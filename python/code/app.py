#!/usr/bin/env python

from os import environ as env
from redis import Redis

redis_host = env.get("REDIS_HOST", "redis")

def check_connection():
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
    check_connection()