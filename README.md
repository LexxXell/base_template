# **This is a docker-compose based application template.**

**All used docker images are built on the basis of Alpine OS, it is unacceptable to use images built on the basis of other OS due to incompatibility with package managers.**

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
