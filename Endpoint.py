from flask import Flask, Response
from flask import request

from werkzeug.middleware.proxy_fix import ProxyFix

import json

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/process", methods=['POST'])
def process():
    return Response("processed")
