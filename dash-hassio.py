import datetime
import logging
#import urllib
#import urllib2
#import base64
import sys
import datetime
import time
import os


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


# Constants and global vars
timespan_threshhold = 39
lastpress           = {}

def arp_display(pkt):
  button = 'no-arp-op-1'
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: # who-has (request)

      # This button is just for the following structure 
      # so that all ral buttons begin with "elif" 
      if pkt[ARP].hwsrc == '23:45:67:89:01:23':
        button = 'shouldntexist'
      
      # <begin section button definitions>
      elif pkt[ARP].hwsrc == 'ac:63:be:44:51:b3':
        button = 'Ariel1'

      elif pkt[ARP].hwsrc == 'ac:63:be:1f:e7:fd':
        button = 'Bio1'

      elif pkt[ARP].hwsrc == '50:f5:da:07:64:71':
        button = 'Bio2'

      elif pkt[ARP].hwsrc == 'ac:63:be:a3:5c:03':
        button = 'Caffe1'

      elif pkt[ARP].hwsrc == '50:f5:da:de:d2:82':
        button = 'Finish1'

      elif pkt[ARP].hwsrc == 'ac:63:be:72:fa:13':
        button = 'Finish2'

      elif pkt[ARP].hwsrc == 'ac:63:be:17:1e:87':
        button = 'Kleenex1'

      elif pkt[ARP].hwsrc == 'ac:63:be:b8:17:39':
        button = 'Persil1'

      elif pkt[ARP].hwsrc == 'ac:63:be:e3:3c:64':
        button = 'Somat1'

      # <end section button definitions>

      # The following is implemented because I have a device 
      # that causes a lot of arp traffic and I wanted to log this separately
      elif pkt[ARP].hwsrc == 'f8:1a:67:25:36:3a':
        button = 'strange-device'
      else:
        button = 'unknown'

  if button == 'no-arp-op-1':
    sys.stdout.write('.')
  elif button == 'strange-device':
    sys.stdout.write(',')
  elif button == 'unknown':
    sys.stdout.write(';')
    #print " "
    #print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
  
  else: # A relevant button was pressed
    thistime = datetime.datetime.now()
    print ("")
    print (button, "was pressed now at", thistime)
    
    if lastpress.has_key(button):
      lasttime = lastpress[button]
      print (button, "was pressed before at", lasttime)
      timespan = thistime - lasttime
      print ("timespan =", timespan.total_seconds())
      if timespan.total_seconds() > timespan_threshhold:
        trigger(button)
      else:
        print ("No further action because timespan is shorter than", timespan_threshhold, "seconds.")
    else:
      print (button, "was never pressed before.")
      trigger (button)

    lastpress[button] = thistime



# Version for: home assistant / http post / event
def trigger(button):

  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  password = os.getenv('HB_HASSIO_API_PASSWORD', 'unknown')
  data     = """ '{{ "state": true, "attributes": {{"button": "{}"}}  }}' """.format(button)
  url      = "http://hassio.internal:8123/api/events/button-pushed"

  print ("Making HTTP request for:", button)
  print ("p1: url = " + url)

  curl(password, data, url)  



def curl(password, data, url):
  cmd = """ curl -X POST -H "x-ha-access: {}" -H "Content-Type: application/json"  -d {} {} """.format(password, data, url)
  print ("cmd = <<< " + cmd + " >>>")
  print ("")
  print ("The next line is the servers returned payload")
  result = os.system(cmd)
  print ("")
  print ("Result of OS command should be 0 and it is '" + str(result) + "'")
  print ("")




print ("Running dash-filter.py version 21")
print ("Waiting for an amazon dash button to register to the network ...")
print ("")

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()

# eof
