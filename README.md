# **This is a docker-compose based application template.**

**All used docker images are built on the basis of Alpine OS, it is unacceptable to use images built on the basis of other OS due to incompatibility with package managers.**

## **Supported platforms:**
* Python
* NodeJS

## **Git branches**
| Branch     | Disrcription                                                              |
|------------|---------------------------------------------------------------------------|
| base       | This is the base branch. Merge the desired branch here and start working. |
| python     | If you only need Python, use this branch.                                 |
| nodejs     | If you only need NodeJS, use this branch.                                 |
| nginx      | If you only need NGINX, use this branch.                                  |
| postgres   | If you only need PostgreSQL DBMS, use this branch.                        |
| redis      | If you only need Redis, use this branch.                                  |
| pgrd       | PostgreSQL DBMS, Redis server                                             |
| nong       | NodeJS and configured NGINX                                               |
| nopg       | NodeJS and PostgreSQL DBMS                                                |
| nord       | NodeJS, Redis server                                                      |
| nopgrd     | NodeJS, PostgreSQL DBMS, Redis server                                     |
| nongpg     | NodeJS, PostgreSQL DBMS and configured NGINX                              |
| nongrd     | NodeJS, Redis server and configured NGINX                                 |
| nongpgrd   | NodeJS, PostgreSQL DBMS, Redis server and configured NGINX                |
| pyng       | Python and configured NGINX                                               |
| pypg       | Python, PostgreSQL DBMS                                                   |
| pyrd       | Python, Redis server                                                      |
| pypgrd     | Python, PostgreSQL DBMS, Redis server                                     |
| pyngpg     | Python, PostgreSQL DBMS and configured NGINX                              |
| pyngrd     | Python, Redis server and configured NGINX                                 |
| pyngpgrd   | Python, PostgreSQL DBMS, Redis server and configured NGINX                |
| pyno       | Python and NodeJS                                                         |
| pynong     | Python, NodeJS and configured NGINX                                       |
| pynopg     | Python, NodeJS, PostgreSQL DBMS                                           |
| pynord     | Python, NodeJS, Redis server                                              |
| pynopgrd   | Python, NodeJS, PostgreSQL DBMS, Redis server                             |
| pynongpg   | Python, NodeJS, PostgreSQL DBMS and configured NGINX                      |
| pynongrd   | Python, NodeJS, Redis server and configured NGINX                         |
| pynongpgrd | Python, NodeJS, PostgreSQL DBMS, Redis server and configured NGINX        |


## **Virtual environment variables**

### Base variables
    USER_NAME=user1
    USER_ID=1001
    HOME_DIR=/home/app
    OS_DEPS=

### NGINX
    NGINX_IMAGE_VERSION=1.19-alpine
    VIRTUAL_HOST=localhost, 127.0.0.1
    API_PORT=8000

### Python
    PYTHON_IMAGE_VERSION=3.9.5-alpine
    PIPENV_DEV=false
    PYTHON_OS_DEPS=postgresql-dev gcc python3-dev musl-dev

### NodeJS
    NODE_IMAGE_VERSION=17-alpine
    NODE_LAUNCH_COMMAND=yarn run dev
    NODE_OS_DEPS=

### PostgreSQL
    POSTGRES_IMAGE_VERSION=13-alpine
    POSTGRES_PASSWORD=postgres
    POSTGRES_USER=postgres
    POSTGRES_HOST=postgres
    POSTGRES_DB=postgres

### Redis server
    REDIS_IMAGE_VERSION=6.2-alpine
    REDIS_HOST=redis