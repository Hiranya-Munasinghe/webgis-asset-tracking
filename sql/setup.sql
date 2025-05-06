-- Active: 1746462519117@@localhost@5432@asset_tracking@public
-- Active: 1746462519117@@localhost@5432@asset_tracking@public
CREATE EXTENSION postgis;

CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    location GEOMETRY(Point, 4326),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO assets (name, description, location) VALUES
('Truck 1', 'Delivery Truck', ST_SetSRID(ST_MakePoint(79.8612, 6.9271), 4326)),
('Truck 2', 'Maintenance Truck', ST_SetSRID(ST_MakePoint(79.8650, 6.9275), 4326)),
('Car 1', 'Service Car', ST_SetSRID(ST_MakePoint(79.8670, 6.9280), 4326)),
('Bike 1', 'Courier Bike', ST_SetSRID(ST_MakePoint(79.8690, 6.9290), 4326)),
('Drone 1', 'Survey Drone', ST_SetSRID(ST_MakePoint(79.8700, 6.9300), 4326));

SELECT * FROM assets;

DELETE FROM assets WHERE id BETWEEN 6 AND 10;

ALTER TABLE assets ADD COLUMN status VARCHAR(20) DEFAULT 'Active';

