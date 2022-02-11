#SSH

FROM cueh/debian_ctf

#Add a user
RUN useradd -ms /bin/bash cueh && useradd -ms /bin/bash heuc && useradd -ms /bin/bash admin && echo cueh:cueh | chpasswd

#Install Global Programs
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server

#Configure SSH (Cant run as Daemon if this doenst exit
RUN mkdir /var/run/sshd

ADD --chown=heuc:heuc heuc /home/heuc
ADD --chown=admin:admin admin /home/admin

RUN cp /usr/bin/tee /home/cueh/ && chown admin:admin /home/cueh/tee && chmod a+s /home/cueh/tee

# PORTS AND BASIC COMMAND
#RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

