from marshmallow import Schema, fields


class HelloWorldSchema(Schema):
    message = fields.Str()