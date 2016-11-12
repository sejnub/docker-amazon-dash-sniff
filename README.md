# amazon-dash-sniff

Image on hub.docker: https://hub.docker.com/r/sejnub/amazon-dash-sniff/

This is a Dockerfile for the hack described in https://blog.thesen.eu/aktuellen-dash-button-oder-ariel-etc-von-amazon-jk29lp-mit-dem-raspberry-pi-nutzen-hacken/

## Prepare rpi
Prepare rpi as described in http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/

To test: 
```
docker run -ti resin/rpi-raspbian:jessie-20160831 /bin/bash
```

## Build image from GitHub

```
cd ..
rm -rf docker-amazon-dash-sniff
git clone https://github.com/sejnub/docker-amazon-dash-sniff.git
cd docker-amazon-dash-sniff 
docker build -t sejnub/amazon-dash-sniff .
```

## Run it

To run it for test purposes with attached console:
```
docker run --net host -it --env-file /hb-credentials.env sejnub/amazon-dash-sniff /bin/bash
```

To run it for production:
```
docker run --net host -d --env-file /hb-credentials.env sejnub/amazon-dash-sniff
```

## Push it

To push it to hub.docker.com:
```
docker login
docker push sejnub/amazon-dash-sniff
```

## clips

```
cd ..
rm -rf docker-amazon-dash-sniff
git clone https://github.com/sejnub/docker-amazon-dash-sniff.git
cd docker-amazon-dash-sniff 
docker build -t sejnub/amazon-dash-sniff .

docker rm -f sejnub/amazon-dash-sniff; docker run --net host -it --env-file /hb-credentials.env sejnub/amazon-dash-sniff /bin/bash

```
