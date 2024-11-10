from marshmallow import Schema, fields, validate


class SensorMeasurementV1Schema(Schema):
    time = fields.Integer(
        required=True,
        description="Timestamp em formato epoch",
        validate=validate.Range(min=0),
    )
    internalHumidity = fields.Float(
        required=True,
        description="Umidade interna em percentagem",
        validate=validate.Range(min=0.0, max=100.0),
    )
    externalHumidity = fields.Float(
        required=True,
        description="Umidade externa em percentagem",
        validate=validate.Range(min=0.0, max=100.0),
    )
    internalTemperature = fields.Float(
        required=True, description="Temperatura interna em graus Celsius"
    )
    externalTemperature = fields.Float(
        required=True, description="Temperatura externa em graus Celsius"
    )
    luminosity = fields.Integer(
        required=True,
        description="Nível de luminosidade",
        validate=validate.Range(min=0, max=1023),
    )
    batteryLevel = fields.Float(
        description="Nível da bateria em percentagem",
        validate=validate.Range(min=0.0, max=100.0),
    )



def handle_validation_error(err):
    error_messages = []
    for field, messages in err.messages.items():
        error_messages.append(f"Field '{field}': {', '.join(messages)}")
    return {"errors": error_messages}, 400


class HelloWorldSchema(Schema):
    message = fields.Str()
