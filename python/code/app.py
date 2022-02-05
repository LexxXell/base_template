#!/usr/bin/env python

from os import environ as env
from flask import Flask, jsonify
from flask_cors import CORS
from redis import Redis

app = Flask(__name__)
CORS(app)

api_port = env.get("API_PORT", 8000)
redis_host = env.get("REDIS_HOST", "redis")

@app.route("/api_v1_py/")
def check_api():
    return jsonify({ "error": False, "message": "API.v1 is available" })

@app.route("/api_v1_py/check_redis")
def check_redis():
    _error = False
    _msg = ""
    try:
        print('Connecting to the Redis server...')
        conn = Redis(host=redis_host)
        redis_info = conn.info()
        print('Redis server version:')
        _msg = f"Redis version: {redis_info['redis_version']}; " + \
            f"Redis mode: {redis_info['redis_mode']}; " + \
                f"GCC version: {redis_info['gcc_version']}; " + \
                    f" OS: {redis_info['os']} x{redis_info['arch_bits']}"
        print(_msg)
    except Exception as error:
        _error = True
        _msg = str(error)
        print(error)
    return jsonify({ "error": _error, "message": _msg })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=api_port)
