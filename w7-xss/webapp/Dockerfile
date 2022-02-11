FROM cueh/flask

# In CUEH/flask we have flask as the defalt user
# Lets make it root for the moment

USER root  

RUN apt-get update && apt-get install -y --no-install-recommends php-cli

#Install the Selenium Driver
COPY REQUIREMENTS.txt /tmp/REQUIREMENTS.txt
RUN pip install -r /tmp/REQUIREMENTS.txt


WORKDIR /opt
#COPY ./xss_trainer /opt/xss_trainer
