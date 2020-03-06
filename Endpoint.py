from flask import Flask, Response
from flask import request

from werkzeug.middleware.proxy_fix import ProxyFix

from ProcessingRequest import ProcessingRequest
from BERTRequest import BERTRequest

import json

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.config["LABTWIN_RATIO"] = 0.2
app.config["LABTWIN_DEFAULT_MIN_LENGTH"] = 10
app.config["LABTWIN_DEFAULT_MAX_LENGTH"] = 100

@app.route("/process", methods=['POST'])
def process():
    req_type = request.headers.get("Content-Type")
    if req_type != "application/json":
        return Response(status=400)
    req_json = request.get_json()
    req = ProcessingRequest(
        "",
        app.config["LABTWIN_RATIO"],
        app.config["LABTWIN_DEFAULT_MIN_LENGTH"],
        app.config["LABTWIN_DEFAULT_MAX_LENGTH"])

    req.from_json(req_json)

    bert_req = BERTRequest(req)
    summary = bert_req.request()
    
    response = Response(json.dumps({"summary": summary}))
    response.content_type = "application/json"
    return response
