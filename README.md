# docker-amazon-dash-sniff

Prepare rpi as described in http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/

To test: 
```
docker run -ti resin/rpi-raspbian:jessie-20160831 /bin/bash
```

This is a Dockerfile for the hack described in https://blog.thesen.eu/aktuellen-dash-button-oder-ariel-etc-von-amazon-jk29lp-mit-dem-raspberry-pi-nutzen-hacken/

```
git clone https://github.com/sejnub/docker-amazon-dash-sniff.git
cd docker-amazon-dash-sniff 
docker build -t amazon-dash-sniff .
```
