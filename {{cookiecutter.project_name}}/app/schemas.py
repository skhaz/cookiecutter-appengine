# -*- coding: utf-8 -*-
from marshmallow import Schema, fields


class BaseSchema(Schema):

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many):
        return {'result': data} if many else data


class UserSchema(BaseSchema):
    key = fields.Function(lambda obj: obj.key.urlsafe())
    name = fields.String()
    email = fields.String()
    avatar = fields.String()
    last_seen = fields.DateTime(dump_only=True, load_from='updated')
