FROM resin/rpi-raspbian:jessie-20160831  

RUN apt-get -qy update && \
    apt-get -qy install python-scapy \
                        tcpdump \
                        tcpreplay # really necessary?
    
COPY dash.py        /usr/local/bin
COPY dash-filter.py /usr/local/bin

CMD ["python", "/usr/local/bin/dash.py"] 
