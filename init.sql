CREATE DATABASE estufa_001;

\c estufa_001;

CREATE TABLE sensors_catalog (
    id SERIAL PRIMARY KEY,
    sensor_type TEXT NOT NULL CHECK (sensor_type IN ('temperature', 'humidity', 'luminosity')),
    sensor_name TEXT NOT NULL,
    location TEXT,
    unit TEXT,
    installation_date DATE,
    status TEXT NOT NULL CHECK (status IN ('active', 'inactive'))
);

CREATE TABLE humidity (
    id INTEGER REFERENCES sensors_catalog(id),
    event_time_unix BIGINT NOT NULL,
    humidity NUMERIC(5,2) NOT NULL CHECK (humidity BETWEEN 0 AND 100),
    PRIMARY KEY (id, event_time_unix)
);

CREATE TABLE temperature (
    sensor_id INTEGER REFERENCES sensors_catalog(id),
    event_time_unix BIGINT NOT NULL,
    temperature NUMERIC(5,2) NOT NULL,
    PRIMARY KEY (sensor_id, event_time_unix)
);

CREATE TABLE luminosity (
    sensor_id INTEGER REFERENCES sensors_catalog(id),
    event_time_unix BIGINT NOT NULL,
    luminosity NUMERIC(5,2) NOT NULL,
    PRIMARY KEY (sensor_id, event_time_unix)
);

INSERT INTO sensors_catalog (sensor_type, sensor_name, status)
VALUES
    ('temperature', 'internalTemperature', 'active'),
    ('humidity', 'internalHumidity', 'active'),
    ('luminosity', 'luminosity', 'active'),
    ('temperature', 'externalTemperature','active'),
    ('humidity', 'externalHumidity', 'active');

