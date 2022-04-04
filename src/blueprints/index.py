import flask
import requests
import json
from flask import Blueprint, render_template

from static.resources.keys import IEX_CLOUD_API_TOKEN

index_page = Blueprint("index", __name__, static_folder="static", template_folder="templates")


@index_page.route('/', methods=["GET", "POST"])
def index():
    """
    This method returns the index page.
    :return: render_template('index.html')
    """

    symbol = 'AAPL'
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    # api_url = f'https://cloud.iexapis.com/stable/account/metadata?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()


    return flask.jsonify(**data)
    # return render_template('index.html', data=data)
