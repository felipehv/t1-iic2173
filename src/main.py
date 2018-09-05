# Flask Libs
from flask import Flask
from flask import request, Response, send_from_directory, render_template, request
from flask_cors import CORS, cross_origin
# System libs
import json
# Other libs
from .db import DB
# from functions import *

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET", "POST", "PUT"])
def ruta():
    # Para evitar problemas con Chrome
    resp.headers['Access-Control-Allow-Origin'] = '*'

    if request.method == "GET":
        result = 'GET request is not allowed'
        status = 501

    elif request.method == "POST":
        db = DB() # DB se ve en la siguiente sección.
        result = db.some_query(request.get_json(force=True)) # get_json entrega
                                                             # el json de la request
        status = 200
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    return resp

