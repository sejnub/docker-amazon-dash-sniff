# amazon-dash-sniff

Image on hub.docker: https://hub.docker.com/r/sejnub/amazon-dash-sniff/

This is a Dockerfile for the hack described in https://blog.thesen.eu/aktuellen-dash-button-oder-ariel-etc-von-amazon-jk29lp-mit-dem-raspberry-pi-nutzen-hacken/


## Status and rights
This works stable for me. But the code is **specific for my setup** (buttons and HTTP target). 
So if you want to use this you have to change the code. 

I claim no rights to this. Feel free to do with it, what you want!


## Prepare rpi
Prepare rpi as described in http://blog.alexellis.io/getting-started-with-docker-on-raspberry-pi/

To test: 
```
docker run -ti resin/rpi-raspbian:jessie-20160831 /bin/bash
```

## Build image from GitHub

```
cd ~
rm -rf ~/docker-amazon-dash-sniff
git clone https://github.com/sejnub/docker-amazon-dash-sniff.git
cd ~/docker-amazon-dash-sniff 
docker build -t sejnub/amazon-dash-sniff .
```

## Run it

To run it for test purposes with attached console:
```
docker rm -f dash; docker run --net host -it --env-file /usr/local/etc/sejnub-credentials.env --name dash sejnub/amazon-dash-sniff /bin/bash
python /usr/local/bin/dash.py

```

To run it for production:
```
docker rm -f dash; docker run --net host -d --env-file /usr/local/etc/sejnub-credentials.env --name dash sejnub/amazon-dash-sniff
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

docker rm -f dash; docker run --net host -it --env-file /usr/local/etc/sejnub-credentials.env --name dash sejnub/amazon-dash-sniff /bin/bash


python /usr/local/bin/dash.py

```
