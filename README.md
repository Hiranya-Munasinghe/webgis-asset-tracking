# WebGIS Asset Tracking System

This project is a simple **WebGIS asset tracking app** built with:
- Python + Flask backend
- PostgreSQL + PostGIS database
- OpenLayers frontend

It tracks asset locations on a map, updates them every 5 seconds, and displays popup details on click.

---

## 🚀 Features

✅ Red circle markers with white borders  
✅ Name labels above each point  
✅ Smooth auto-refresh every 5 seconds  
✅ Popup with white box + arrow showing **name** and **status**  
✅ Popup disappears when clicking on empty map  

---

## 📦 Setup Instructions

### 1️⃣ Install and configure the database

1. Install PostgreSQL and PostGIS.
2. Create a database:
    ```bash
    createdb asset_tracking
    ```
3. Connect to the database:
    ```bash
    psql -d asset_tracking
    ```
4. Create the `assets` table:
    ```sql
    CREATE TABLE assets (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Active',
        location GEOGRAPHY(Point, 4326),
        updated_at TIMESTAMP DEFAULT NOW()
    );
    ```
5. Insert sample data:
    ```sql
    INSERT INTO assets (name, description, status, location)
    VALUES 
    ('Asset 1', 'First asset', 'Active', ST_SetSRID(ST_MakePoint(79.8612, 6.9271), 4326)),
    ('Asset 2', 'Second asset', 'Active', ST_SetSRID(ST_MakePoint(79.8620, 6.9280), 4326));
    ```

---

### 2️⃣ Set up the Python backend

1. Create a Python virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

2. Install dependencies:
    ```bash
    pip install flask flask-cors psycopg2
    ```

3. Update `app.py` with your **DB credentials**:
    ```python
    DB_HOST = "localhost"
    DB_NAME = "asset_tracking"
    DB_USER = "postgres"
    DB_PASS = "your_password"
    ```

4. Run the backend:
    ```bash
    python app.py
    ```

Backend will start at: [http://localhost:5000](http://localhost:5000)

---

### 3️⃣ Run the frontend

1. Save the provided `index.html` in your project folder.
   
2. Open `index.html` directly in your web browser **OR**  
   Run a local web server (recommended for best behavior):
    ```bash
    # Python 3.x
    python -m http.server
    ```
    Then visit: [http://localhost:8000](http://localhost:8000)

---

### 4️⃣ Output!

- You’ll see a map with live-updating asset markers.
- Click a marker to see its popup.
- Click an empty area to close the popup.
- Every 5 seconds, locations will randomly shift and refresh.

---

