FROM cueh/flask

USER root
RUN apt-get update && apt-get install -y --no-install-recommends ncat

USER flask
WORKDIR /opt
ADD ./opt /opt