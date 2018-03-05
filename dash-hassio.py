import datetime
import logging
#import urllib
#import urllib2
#import base64
import sys
import datetime
import time
import os
#import pytz
#from datetime import timezone

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


# Constants and global vars
timespan_threshhold  = 39
lastpress            = {}
heartbeat_threshhold = 90


one_day = datetime.timedelta(days=1)
heartbeat_lasttime = datetime.datetime.now() - one_day

print ("p3: heartbeat_lasttime: {}".format(heartbeat_lasttime))


def arp_display(pkt):
  global timespan_threshhold 
  global lastpress           
  global heartbeat_threshhold
  global heartbeat_lasttime 

  button = 'no-arp-op-1'
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: # who-has (request)

      # This button is just for the following structure 
      # so that all ral buttons begin with "elif" 
      if pkt[ARP].hwsrc == '23:45:67:89:01:23':
        button = 'shouldntexist'
      
      # <begin section button definitions>
      elif pkt[ARP].hwsrc == 'ac:63:be:44:51:b3':
        button = 'ariel1'

      elif pkt[ARP].hwsrc == 'ac:63:be:1f:e7:fd':
        button = 'bio1'

      elif pkt[ARP].hwsrc == '50:f5:da:07:64:71':
        button = 'bio2'

      elif pkt[ARP].hwsrc == 'ac:63:be:a3:5c:03':
        button = 'caffe1'

      elif pkt[ARP].hwsrc == '50:f5:da:de:d2:82':
        button = 'finish1'

      elif pkt[ARP].hwsrc == 'ac:63:be:72:fa:13':
        button = 'finish2'

      elif pkt[ARP].hwsrc == 'ac:63:be:17:1e:87':
        button = 'kleenex1'

      elif pkt[ARP].hwsrc == 'ac:63:be:b8:17:39':
        button = 'persil1'

      elif pkt[ARP].hwsrc == 'ac:63:be:e3:3c:64':
        button = 'somat1'

      # <end section button definitions>

      # The following is implemented because I have a device 
      # that causes a lot of arp traffic and I wanted to log this separately
      elif pkt[ARP].hwsrc == 'f8:1a:67:25:36:3a':
        button = 'strange-device'
      else:
        button = 'unknown'

  #print ("p4: heartbeat_lasttime: {}".format(heartbeat_lasttime))
  #print ("p5: timespan_threshhold: {}".format(timespan_threshhold))

  thistime = datetime.datetime.now()
  heartbeat_timespan = thistime - heartbeat_lasttime

  if heartbeat_timespan.total_seconds() > heartbeat_threshhold:
    print("")
    print("I am sendining a heartbeat.")
    trigger_heartbeat(thistime)
    heartbeat_lasttime = thistime

  if button == 'no-arp-op-1':
    sys.stdout.write('.')
  elif button == 'strange-device':
    sys.stdout.write(',')
  elif button == 'unknown':
    sys.stdout.write(';')
    #print " "
    #print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
  
  else: # A relevant button was pressed
    print ("")
    print (button, "was pressed now at", thistime)
    
    if lastpress.has_key(button):
      lasttime = lastpress[button]
      print (button, "was pressed before at", lasttime)
      timespan = thistime - lasttime
      print ("timespan =", timespan.total_seconds())
      if timespan.total_seconds() > timespan_threshhold:
        print (button, "Was pressed before, but long ago. action!")
        trigger(button)
      else:
        print ("No further action because timespan is shorter than", timespan_threshhold, "seconds.")
    else:
      print (button, "Was never pressed before. action!")
      trigger(button)

    lastpress[button] = thistime


# https://home-assistant.io/developers/rest_api/#post-apiservicesltdomainltservice
# Version for: home assistant / http post / service
# POST /api/services/<domain>/<service>
def trigger_heartbeat(thistime):
  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  url      = "http://hassio.internal:8123/api/services/input_label/set_value"
  # TODO: Convert to localtime in next line
  data     = """ '{{ "entity_id": "input_label.dashbutton_heartbeat", "value": "{:%Y-%m-%dT%H:%M:%S}Z" }}' """.format(thistime)
  print ("Making HTTP request for heartbeat")
  print ("p2: url = " + url)
  curl(data, url)  


# https://home-assistant.io/developers/rest_api/#post-apiservicesltdomainltservice
# Version for: home assistant / http post / service
# POST /api/services/<domain>/<service>
def trigger(button):
  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  url      = "http://hassio.internal:8123/api/services/input_label/set_value"
  # TODO: Convert to localtime in next line
  data     = """ '{{ "entity_id": "input_label.dashbutton_{}", "value": "{:%Y-%m-%dT%H:%M:%S}Z" }}' """.format(button, datetime.datetime.now())
  print ("Making HTTP request for:", button)
  print ("p1: url = " + url)
  curl(data, url)  


# https://home-assistant.io/developers/rest_api
# Version for: home assistant / http post / state
def trigger_state(button):

  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  data     = """ '{{ "state": "on", "attributes": {{"button": "{}"}}  }}' """.format(button)
  
  # post tequest to /api/states/<entity_id> 
  # e.g. entity: sensor.dashbutton_caffe1
  url      = "http://hassio.internal:8123/api/states/sensor.dashbutton_{}".format(button)

  print ("Making HTTP request for:", button)
  print ("p1: url = " + url)

  curl(data, url)  


# https://home-assistant.io/developers/rest_api
# Version for: home assistant / http post / event
def trigger_event(button):
  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  url      = "http://hassio.internal:8123/api/events/button-pushed"
  data     = """ '{{ "state": true, "attributes": {{"button": "{}"}}  }}' """.format(button)
  print ("Making HTTP request for:", button)
  print ("p1: url = " + url)
  curl(data, url)  


def trigger_service_1(button):
  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  url      = "http://hassio.internal:8123/api/services/input_boolean/turn_on"
  data     = """ '{{ "entity_id": "input_boolean.dashbutton_{}" }}' """.format(button)
  print ("Making HTTP request for:", button)
  print ("p1: url = " + url)
  curl(data, url)  



def curl(data, url):
  password = os.getenv('HB_HASSIO_API_PASSWORD', 'unknown')
  cmd = """ curl -X POST -H "x-ha-access: {}" -H "Content-Type: application/json"  -d {} {} """.format(password, data, url)
  print ("cmd = <<< " + cmd + " >>>")
  print ("")
  print ("The next line is the server's returned payload")
  result = os.system(cmd)
  print ("")
  print ("Result of OS command should be 0 and it is '" + str(result) + "'")
  print ("")



print ("Running dash-filter.py version 22")
print ("Waiting for an amazon dash button to register to the network ...")
print ("")

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()

# eof
