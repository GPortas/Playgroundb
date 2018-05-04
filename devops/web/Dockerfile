FROM ubuntu:16.04
ENTRYPOINT npm run start
USER root
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        nodejs \
        build-essential
RUN mkdir -p /opt/pdb/web
WORKDIR /opt/pdb/web
ADD web/package.json .
RUN npm install ; exit 0
ADD web/public ./public
ADD web/src ./src
RUN npm install crypto-js
RUN npm install universal-cookie

