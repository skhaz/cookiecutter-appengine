# -*- coding: utf-8 -*-
from flask import Blueprint, abort, request, render_template
from app.kernel.cache import cache

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/')
@cache.cached()
def index():
    return render_template('index.html')
