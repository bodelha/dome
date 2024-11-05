from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schema import HelloWorldSchema, SensorMeasurementV1Schema, handle_validation_error
from db import Database

app = Flask(__name__)
db = Database()


@app.route('/v1/measurements', methods=['POST'])
def receive_measurements():
    schema = SensorMeasurementV1Schema()
    try:
        data = schema.load(request.json)
        db.connect()
        query = f"INSERT INTO your_table_name (field1, field2, ...) VALUES (%s, %s, ...)"
        params = tuple(data.values())
        db.execute(query, params)
        db.conn.commit()
        db.close()
        return jsonify({"message": "Medições recebidas e salvas com sucesso!", "data": data}), 201
    except ValidationError as err:
        return handle_validation_error(err)
    except Exception as e:
        print(f"An error occurred while persisting data: {e}")
        return jsonify({"message": "Erro ao salvar os dados."}), 500


@app.route('/', methods=['GET'])
def hello_world():
    response_data = {"message": "Hello, World!"}
    
    schema = HelloWorldSchema()
    result = schema.dump(response_data)

    return jsonify(result)

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True)
