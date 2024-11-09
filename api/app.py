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
            app.logger.info(field)
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


@app.route('/', methods=['GET'])
def hello_world():
    response_data = {"message": "Hello, World!"}
    
    schema = HelloWorldSchema()
    result = schema.dump(response_data)

    return jsonify(result)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)
