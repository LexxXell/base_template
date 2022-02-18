# **This is a docker-compose based application template.**

**All used docker images are built on the basis of Alpine OS, it is unacceptable to use images built on the basis of other OS due to incompatibility with package managers.**

---

## **Supported platforms:**
* Python
* NodeJS
---
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

Branches containing NGINX, when launched, raise a web server at http://localhost


For branches containing NGINX to work, you need to run a reverse proxy server from the proxy directory.

    docker-compose -f proxy/docker-compose.yml up -d

---
## **Virtual environment variables**
***Default values ​​specified***

**Items marked with (*) should only be changed if you understand what you are doing.**

### Base variables

Distributed for platform containers (Python, NodeJS)

Use the user and user ID under which the application is launched. This is necessary for correct access to files on mounted volumes.

    USER_NAME=user1
    USER_ID=1001

(*) You can specify the desired home directory in the container.

    HOME_DIR=/home/app

Specify the necessary AlpineOS system dependencies separated by spaces. Will be used for all platforms.

    OS_DEPS=

### NGINX

Select the desired version of NGINX (based on AlpineOS) at https://hub.docker.com

    NGINX_IMAGE_VERSION=1.19-alpine

Specify comma-separated domain names for the web server.

    VIRTUAL_HOST=localhost, 127.0.0.1

(*) You can specify the API port in the container.

    API_PORT=8000

### Python

Select the desired version of Python (based on AlpineOS) at https://hub.docker.com

    PYTHON_IMAGE_VERSION=3.9.5-alpine

(*) If PipENV is used, this variable enables --dev packages to be installed.

    PIPENV_DEV=false

Specify the necessary AlpineOS system Python dependencies separated by spaces.

    PYTHON_OS_DEPS=postgresql-dev gcc python3-dev musl-dev

### NodeJS

Select the desired version of NodeJS (based on AlpineOS) at https://hub.docker.com

    NODE_IMAGE_VERSION=17-alpine

(*) NodeJS project start command.

    NODE_LAUNCH_COMMAND=yarn run dev

Specify the necessary AlpineOS system NodeJS dependencies separated by spaces.

    NODE_OS_DEPS=

### PostgreSQL

Select the desired version of PostgreSQL (based on AlpineOS) at https://hub.docker.com

    POSTGRES_IMAGE_VERSION=13-alpine

(*) PostreSQL global settings. Will be used for all platforms.

    POSTGRES_PASSWORD=postgres
    POSTGRES_USER=postgres
    POSTGRES_HOST=postgres
    POSTGRES_DB=postgres

### Redis server

Select the desired version of Redis server (based on AlpineOS) at https://hub.docker.com

    REDIS_IMAGE_VERSION=6.2-alpine

(*) Redis global settings. Will be used for all platforms.

    REDIS_HOST=redis
---
## **USAGE**

Let's take an example.
You have written an application using Python, NodeJS, Postgres, Redis and want to use NGINX as a web server. (pynongpgrd)
You can use the XTMPL wrapper https://github.com/LexxXell/xtmpl or work with the template directly.

Clone branch of the template into the project dir.

    git clone --branch=pynongpgrd https://github.com/LexxXell/base_template.git .
    git remote remove origin

Run a reverse proxy server from the proxy directory.

    docker-compose -f proxy/docker-compose.yml up -d

Checking the work of the cloned branch:

    docker-compose up --build

Check the  output to the console, and for branches containing NGINX, we additionally go to the browser at http://localhost

Customize the database connection in your applications following the example in the python/code and nodejs/code directories.
Move your application code to the python/code and nodejs/code directories, after deleting the app,js/app.py files from there.
Customize .env file to your liking.

For security reasons, after making changes to the code, you need to rebuild the containers.
All management of starting, building and stopping containers is done using docker-compose.

To implement autostart, you need to add for the required services to the docker-compose.yml file

    restart: always
