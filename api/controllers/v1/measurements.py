from flask import request, jsonify
from marshmallow import ValidationError
from db import Database
from schema import SensorMeasurementV1Schema
from utils import log_error
from psycopg2 import sql

def save_measurements():
    schema = SensorMeasurementV1Schema()
    db = Database()

    try:
        data = schema.load(request.json)
        db.connect()

        for field in data:
            if field in ("time", "batteryLevel"):
                continue

            query = """
                SELECT id, sensor_type 
                FROM sensors_catalog 
                WHERE sensor_name = %s AND status = 'active';
            """
            sensor_info = db.fetchone(query, (field,))
            if not sensor_info:
                raise ValueError(f"Sensor {field} não encontrado ou inativo.")

            sensor_id, table_name = sensor_info

            insert_query = sql.SQL("""
                INSERT INTO {table} (sensor_id, event_time_unix, {column})
                VALUES (%s, %s, %s)
            """).format(
                table=sql.Identifier(table_name),
                column=sql.Identifier(table_name)
            )

            db.execute(insert_query, (sensor_id, data["time"], data[field]))

        db.conn.commit()
        return jsonify({"message": "Medições recebidas e salvas com sucesso!", "data": data}), 201

    except ValidationError as err:
        return jsonify({"message": "Erro de validação", "errors": err.messages}), 400
    except Exception as e:
        log_error(e)
        return jsonify({"message": "Erro interno ao salvar as medições."}), 500
    finally:
        db.close()


def get_measurements():
    limit = request.args.get("limit", default=10, type=int)
    offset = request.args.get("offset", default=0, type=int)
    db = Database()

    try:
        db.connect()

        query = """
            SELECT
                COALESCE(h.event_time_unix, e_h.event_time_unix, t.event_time_unix, e_t.event_time_unix, l.event_time_unix) AS time,
                MAX(h.humidity) AS internalHumidity,
                MAX(e_h.humidity) AS externalHumidity,
                MAX(t.temperature) AS internalTemperature,
                MAX(e_t.temperature) AS externalTemperature,
                MAX(l.luminosity) AS luminosity
            FROM
                sensors_catalog sc
            LEFT JOIN humidity h ON sc.id = h.sensor_id AND sc.sensor_name = 'internalHumidity'
            LEFT JOIN humidity e_h ON sc.id = e_h.sensor_id AND sc.sensor_name = 'externalHumidity'
            LEFT JOIN temperature t ON sc.id = t.sensor_id AND sc.sensor_name = 'internalTemperature'
            LEFT JOIN temperature e_t ON sc.id = e_t.sensor_id AND sc.sensor_name = 'externalTemperature'
            LEFT JOIN luminosity l ON sc.id = l.sensor_id AND sc.sensor_name = 'luminosity'
            WHERE sc.status = 'active'
            GROUP BY time
            ORDER BY time DESC
            LIMIT %s OFFSET %s;
        """

        measurements = db.execute(query, (limit, offset)).fetchall()

        formatted_measurements = []
        for entry in measurements:
            formatted_measurement = {
                "time": entry[0],
                "internalHumidity": entry[1],
                "externalHumidity": entry[2],
                "internalTemperature": entry[3],
                "externalTemperature": entry[4],
                "luminosity": entry[5],
            }
            formatted_measurements.append(formatted_measurement)

        schema = SensorMeasurementV1Schema(many=True)
        result = schema.dump(formatted_measurements)

        return jsonify({"data": result, "limit": limit, "offset": offset}), 200

    except Exception as e:
        log_error(e)
        return jsonify({"message": "Erro ao recuperar os dados."}), 500
    finally:
        db.close()