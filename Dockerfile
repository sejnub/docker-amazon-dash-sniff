FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy update && \
    apt-get -qy install python-scapy \
                        tcpdump      \
                        nano         \
                        tcpreplay #  nano is only for development. tcpreplay really necessary?

RUN apt-get -qy install curl 

COPY dash.py        /usr/local/bin

CMD ["python", "/usr/local/bin/dash.py"] 
