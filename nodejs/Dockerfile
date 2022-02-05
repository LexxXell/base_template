ARG NODE_IMAGE_VERSION=17-alpine
FROM node:$NODE_IMAGE_VERSION

LABEL maintainer="lexxxell007@gamil.com"

ARG USER_NAME=user1
ARG USER_ID=1001
ARG HOME_DIR=/home/app
ARG OS_DEPS

ARG NODE_OS_DEPS
ARG NODE_LAUNCH_COMMAND

ENV APP_HOME=$HOME_DIR
ENV LAUNCH_CMD=$NODE_LAUNCH_COMMAND

RUN apk update && apk --no-cache add \
    tini \
    shadow \
    $OS_DEPS \
    $NODE_OS_DEPS

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

COPY ./code/ .
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN npm i -g npm && npm i yarn && yarn install

RUN addgroup -S $USER_NAME && adduser -S $USER_NAME -G $USER_NAME; \
    groupmod -g $USER_ID $USER_NAME && usermod -u $USER_ID -g $USER_ID $USER_NAME; \
    chown -R $USER_NAME:$USER_NAME $APP_HOME
USER $USER_NAME

ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]