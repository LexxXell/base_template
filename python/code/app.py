#!/usr/bin/env python
import psycopg2
from redis import Redis
from os import environ as env

pg_host = env.get("POSTGRES_HOST", "postgres")
pg_user = env.get("POSTGRES_USER", "postgres")
pg_pass = env.get("POSTGRES_PASSWORD","postgres")
pg_db = env.get("POSTGRES_DB","postgres")

redis_host = env.get("REDIS_HOST", "redis")

def check_pg_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=pg_host,
            database=pg_db,
            user=pg_user,
            password=pg_pass
        )
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def check_redis_connection():
    """ Connect to the Redis server """
    try:
        
        # connect to the Redis server
        print('Connecting to the Redis server...')
        conn = Redis(host=redis_host)
        
	    # execute a statement
        print('Redis server version:')
        redis_info = conn.info()

        # display the Redis server version
        print(f"Redis version: {redis_info['redis_version']}; " + \
            f"Redis mode: {redis_info['redis_mode']}; " + \
                f"GCC version: {redis_info['gcc_version']}; " + \
                    f" OS: {redis_info['os']} [x{redis_info['arch_bits']}]"
        )

        print("[INFO] Connection success!")

    except Exception as error:
        print(error)


if __name__ == '__main__':
    check_pg_connection()
    check_redis_connection()