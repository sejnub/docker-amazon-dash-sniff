FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy update && \
    apt-get -qy install python-scapy \
                        tcpdump      \
                        nano         \
                        tcpreplay    \ #  nano is only for development. tcpreplay really necessary?
                        python3-tz
                        
RUN apt-get -qy install curl 

COPY dash-hassio.py /usr/local/bin
COPY dash-test.py   /usr/local/bin
COPY dash-fhem.py   /usr/local/bin

CMD ["python", "/usr/local/bin/dash-hassio.py"] 
