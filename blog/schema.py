from marshmallow import Schema, fields


class PostSchema(Schema):
    author = fields.String()
    title = fields.String()
    text = fields.String(max_length=50)
    created_datetime = fields.DateTime()
    published_datetime = fields.DateTime()