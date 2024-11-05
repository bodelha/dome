from flask import Flask, request, jsonify
from marshmallow import ValidationError
from schema import HelloWorldSchema, SensorMeasurementV1Schema, handle_validation_error

app = Flask(__name__)


@app.route('/v1/measurements', methods=['POST'])
def receive_measurements():
    schema = SensorMeasurementV1Schema()
    try:
        data = schema.load(request.json)
        return jsonify({"message": "Medições recebidas com sucesso!", "data": data}), 200
    except ValidationError as err:
        return handle_validation_error(err)


@app.route('/', methods=['GET'])
def hello_world():
    response_data = {"message": "Hello, World!"}
    
    schema = HelloWorldSchema()
    result = schema.dump(response_data)

    return jsonify(result)

if __name__ == '__main__':
    
    app.run(host="0.0.0.0", port=5000, debug=True)
