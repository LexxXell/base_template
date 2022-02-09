#!/usr/bin/env python

from os import environ as env
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_port = env.get("API_PORT", 8000)

@app.route("/api_v1_py/")
def check_api():
    return jsonify({ "error": False, "message": "API v1 Python is available" })

@app.route("/api_v1_py/check_postgres")
def check_postgres():
    return jsonify({ "error": True, "message": "Not used in this application..." })

@app.route("/api_v1_py/check_redis")
def check_redis():
    return jsonify({ "error": True, "message": "Not used in this application..." })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=api_port)
