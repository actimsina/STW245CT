FROM node:buster-slim

WORKDIR /opt/app

#Requirements
ADD package.json /opt/app
ADD server.js /opt/app

RUN npm install

EXPOSE 3000

RUN apt-get update && apt-get install -y ncat
ADD serverflag.txt /

CMD ["node", "server.js"]