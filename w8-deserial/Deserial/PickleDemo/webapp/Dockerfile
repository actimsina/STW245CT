FROM cueh/flask

USER root  
#Netcat for the Shell
RUN apt-get update && apt-get install -y ncat

WORKDIR /opt

#Copy Files
ADD REQUIREMENTS.txt /opt

#Install Requirements
RUN pip install -r REQUIREMENTS.txt

ADD serverflag.txt /

ADD app.py /opt/webapp/
ADD templates/* /opt/webapp/templates/

CMD ["flask", "run", "--host=0.0.0.0"]

