#!/usr/bin/env python

import psycopg2
from os import environ as env
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_port = env.get("API_PORT", 8000)
pg_host = env.get("POSTGRES_HOST", "postgres")
pg_user = env.get("POSTGRES_USER", "postgres")
pg_pass = env.get("POSTGRES_PASSWORD","postgres")
pg_db = env.get("POSTGRES_DB","postgres")

@app.route("/api_v1_py/")
def check_api():
    return jsonify({ "error": False, "message": "API.v1 is available" })

@app.route("/api_v1_py/check_postgres")
def check_postgres():
    _error = False
    _msg = "Postgres"
    conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=pg_host,
            database=pg_db,
            user=pg_user,
            password=pg_pass
        )
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        _msg = db_version
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        _error = True
        _msg = error
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return jsonify({ "error": _error, "message": _msg })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=api_port)
