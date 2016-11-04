FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy update && \
    apt-get -qy install python-scapy && \
    apt-get -qy install tcpdump && \
    apt-get -qy install tcpreplay # really necessary?
    
COPY dash1.py /usr/local/bin
COPY dash2.py /usr/local/bin


CMD ["python", "/usr/local/bin/dash2.py"] 
