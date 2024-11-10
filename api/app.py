from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schema import HelloWorldSchema, SensorMeasurementV1Schema, handle_validation_error
from db import Database

app = Flask(__name__)
app.logger.setLevel('DEBUG')
db = Database()


@app.route('/v1/measurements', methods=['POST'])
def receive_measurements():
    schema = SensorMeasurementV1Schema()
    try:
        data = schema.load(request.json)
        app.logger.info(data)
        db.connect()
        for field in data:
            if field in ("time", "batteryLevel"):
                continue
            get_table_query = "SELECT id, sensor_type FROM sensors_catalog WHERE sensor_name = %s AND status = 'active';"
            identifier, table = db.execute(get_table_query, (field,)).fetchone()
            insertion_query = f"""
                INSERT INTO {table} (sensor_id, event_time_unix, {table})
                VALUES (%s, %s, %s);
            """
            db.execute(insertion_query, (identifier, data["time"], data[field]))
        db.conn.commit()
        db.close()
        return jsonify({"message": "Medições recebidas e salvas com sucesso!", "data": data}), 201
    except ValidationError as err:
        return handle_validation_error(err)
    except Exception as e:
        app.logger.exception(f"An error occurred while persisting data: {e}")
        return jsonify({"message": "Erro ao salvar os dados."}), 500

@app.route('/v1/measurements', methods=['GET'])
def get_measurements():
    limit = request.args.get('limit', default=10, type=int)
    offset = request.args.get('offset', default=0, type=int)

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

        app.logger.info(measurements)

        formatted_measurements = []
        for entry in measurements:
            formatted_measurement = {
                "time": entry[0],
                "internalHumidity": entry[1],
                "externalHumidity": entry[2],
                "internalTemperature": entry[3],
                "externalTemperature": entry[4],
                "luminosity": entry[5]
            }
            formatted_measurements.append(formatted_measurement)

        app.logger.info(formatted_measurements)

        schema = SensorMeasurementV1Schema(many=True)
        result = schema.dump(formatted_measurements)
        app.logger.info(result)

        db.close()

        return jsonify({"data": result, "limit": limit, "offset": offset}), 200

    except Exception as e:
        app.logger.exception(f"An error occurred while fetching data: {e}")
        return jsonify({"message": "Erro ao recuperar os dados."}), 500


@app.route('/', methods=['GET'])
def hello_world():
    response_data = {"message": "Hello, World!"}
    
    schema = HelloWorldSchema()
    result = schema.dump(response_data)

    return jsonify(result)


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)
