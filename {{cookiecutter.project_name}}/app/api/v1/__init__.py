# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext.restful import Api
from flask.ext.restful.reqparse import RequestParser

pagination = RequestParser()
pagination.add_argument('limit', type=int, default=10)
pagination.add_argument('offset', type=int, default=0)

api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_blueprint)

from . import auth, users  # noqa

api.add_resource(users.UserResource, '/users/<string:key>')
api.add_resource(users.UserListResource, '/users')
