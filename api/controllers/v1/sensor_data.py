from flask import request, jsonify
from db import Database
from schema import SensorExposureV1Schema


def get_sensor_data():
    db = Database()
    fields = request.args.get("fields", None)
    limit = request.args.get("limit", 60, type=int)
    fields = (
        fields.split(",")
        if fields
        else [
            "internalHumidity",
            "externalHumidity",
            "internalTemperature",
            "externalTemperature",
            "luminosity",
        ]
    )

    try:
        db.connect()

        field_mapping = {
            "internalHumidity": "MAX(CASE WHEN sensor_name = 'internalHumidity' THEN value END) AS \"internalHumidity\"",
            "externalHumidity": "MAX(CASE WHEN sensor_name = 'externalHumidity' THEN value END) AS \"externalHumidity\"",
            "internalTemperature": "MAX(CASE WHEN sensor_name = 'internalTemperature' THEN value END) AS \"internalTemperature\"",
            "externalTemperature": "MAX(CASE WHEN sensor_name = 'externalTemperature' THEN value END) AS \"externalTemperature\"",
            "luminosity": "MAX(CASE WHEN sensor_name = 'luminosity' THEN value END) AS \"luminosity\""
        }

        selected_fields = ", ".join([field_mapping[field] for field in fields if field in field_mapping])

        json_fields = ", ".join([f"'{field}', aggregated_data.\"{field}\"" for field in fields])

        query = f"""
            WITH sensor_data AS (
                SELECT 
                    s.sensor_name,
                    s.sensor_type,
                    CASE 
                        WHEN s.sensor_type = 'temperature' THEN t.event_time_unix
                        WHEN s.sensor_type = 'humidity' THEN h.event_time_unix
                        WHEN s.sensor_type = 'luminosity' THEN l.event_time_unix
                    END AS event_time_unix,
                    CASE 
                        WHEN s.sensor_type = 'temperature' THEN t.temperature
                        WHEN s.sensor_type = 'humidity' THEN h.humidity
                        WHEN s.sensor_type = 'luminosity' THEN l.luminosity
                    END AS value
                FROM 
                    sensors_catalog s
                LEFT JOIN temperature t ON s.id = t.sensor_id
                LEFT JOIN humidity h ON s.id = h.sensor_id
                LEFT JOIN luminosity l ON s.id = l.sensor_id
                WHERE 
                    s.status = 'active'
            ),
            aggregated_data AS (
                SELECT 
                    event_time_unix AS time,
                    {selected_fields}
                FROM 
                    sensor_data
                GROUP BY event_time_unix
                ORDER BY event_time_unix DESC
                LIMIT {limit}
            )
            SELECT jsonb_agg(jsonb_strip_nulls(jsonb_build_object({json_fields}))) AS sensor_data, array_agg(time) AS time
            FROM aggregated_data;
        """

        result = db.execute(query).fetchone()

        data = result[0] if result else []
        time_list = result[1] if result else []

        formatted_data = {"time": time_list}
        for field in fields:
            formatted_data[field] = [entry.get(field) for entry in data]

        schema = SensorExposureV1Schema()
        validated_data = schema.dump(formatted_data)

        return jsonify(validated_data), 200

    except Exception as e:
        db.close()
        raise e
    finally:
        db.close()
