# -*- coding:utf8 -*-

from __future__ import unicode_literals

import random

from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask.json import jsonify
from flask_cache import Cache

from scrapers import query_octa_providers


DEBUG = True
CACHE_PERIOD = 60 * 60 * 24

try:
    from local_settings import *
except ImportError:
    pass


app = Flask(__name__, static_url_path='/static')
cache = Cache(app,config={'CACHE_TYPE': 'simple'})


def randint():
    """
    Select random integer between 00 and 99

    :return: integer
    """
    return random.randint(00, 99)


def get_random_prices():
    """
    Generate random price array

    :return: array of prices|[]
    """
    return ['%s.%s' % (randint(), randint()) for i in range(4)]


@app.route('/api/provider-check/<provider>/<car_id>/<certificate_id>/', methods=['GET'])
@cache.cached(timeout=CACHE_PERIOD)
def fetch_prices(provider, car_id, certificate_id):
    """
    Fetch the prices for specific car from specific provider

    :param provider: provider name|str
    :param car_id: car number|str
    :param certificate_id: certificate number|str
    :return: Array of results
    """
    if DEBUG:
        data = get_random_prices()
    else:
        try:
            data = query_octa_providers(provider, car_id, certificate_id)
        except:
            data = []

    return jsonify(data)


@app.route('/', methods=['GET'])
def front_page():
    """
    Render front page template

    :return: rendered contents
    """
    return render_template('base.html')


@app.route('/static/<path:path>', methods=['GET'])
def send_static(path):
    """
    Serve static content from /static directory

    :param path: asset path|str
    :return:
    """
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run()
