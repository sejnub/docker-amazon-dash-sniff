FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy install scapy && \
    apt-get -qy install tcpdump
    
COPY dash.py /usr/local/bin

python /usr/local/bin/dash.py
