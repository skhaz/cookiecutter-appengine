# -*- coding: utf-8 -*-
from google.appengine.ext import ndb


class User(ndb.Model):
    name = ndb.TextProperty()
    email = ndb.StringProperty()
    avatar = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    deleted = ndb.BooleanProperty(default=False)

    def __repr__(self):
        return '<User(name={self.name!r}, email={self.email!r})>'.format(self=self)
