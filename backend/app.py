from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import random

app = Flask(__name__)
CORS(app)

# Database config
DB_HOST = "localhost"
DB_NAME = "asset_tracking"
DB_USER = "postgres"
DB_PASS = "1886_sudari"

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )

@app.route('/assets')
def get_assets():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description, status, ST_X(location), ST_Y(location) FROM assets;")
    rows = cur.fetchall()
    features = []
    for row in rows:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row[4], row[5]]
            },
            "properties": {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "status": row[3]
            }
        })
    cur.close()
    conn.close()
    return jsonify({"type": "FeatureCollection", "features": features})

@app.route('/update')
def update_assets():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, ST_X(location), ST_Y(location) FROM assets;")
    assets = cur.fetchall()
    for asset in assets:
        new_lon = asset[1] + random.uniform(-0.001, 0.001)
        new_lat = asset[2] + random.uniform(-0.001, 0.001)
        cur.execute(
            "UPDATE assets SET location = ST_SetSRID(ST_MakePoint(%s, %s), 4326), updated_at = NOW() WHERE id = %s;",
            (new_lon, new_lat, asset[0])
        )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "updated"})

if __name__ == '__main__':
    app.run(debug=True)
