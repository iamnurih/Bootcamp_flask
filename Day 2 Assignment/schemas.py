from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)