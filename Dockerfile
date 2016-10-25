FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy install scapy && \
    apt-get -qy install tcpdump
    
