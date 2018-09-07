# Flask Libs
from flask import Flask
from flask import request, Response, send_from_directory, render_template, request
from flask_cors import CORS, cross_origin
# System libs
import json
# Other libs
from .db import DB

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET", "POST", "PUT"])
def ruta():
    # Para evitar problemas con Chrome
    if request.method == "GET":
        page = request.args.get('hola') or 1 
        db = DB()
        result = { 'messages' : db.get_queries(page), "next_url" : "{}?p={}".format(request.base_url, page+1)}
        status = 200

    elif request.method == "POST":
        try:
            db = DB()
            result = db.new_message(request)
            status = 201
        except Exception as e:
            status = 400
            result = {'message': 'No message found, send a json with "message" key'}
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

