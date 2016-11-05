import datetime
import logging
import urllib
import urllib2
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def arp_display(pkt):
  button = 'no-arp-op-1'
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: #who-has (request)
      if pkt[ARP].hwsrc == 'ac:63:be:a3:5c:03': 
        button = 'Caffe1'
      elif pkt[ARP].hwsrc == 'ac:63:be:44:51:b3': 
        button = 'Ariel1'
      elif pkt[ARP].hwsrc == 'ac:63:be:e3:3c:64': 
        button = 'Somat1'
      elif pkt[ARP].hwsrc == 'f8:1a:67:25:36:3a': 
        button = 'strange-device'
      else:
        button = 'unknown'
  
  if button == 'no-arp-op-1':
    sys.stdout.write('.')
  elif button == 'strange-device':
    sys.stdout.write(',')
  elif button == 'unknown':
    print " "
    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
  else:
    print " "
    print "Pushed button: " + button

    url = 'http://192.168.178.31:8083/fhem?cmd=set%20DashButton' + button + '%20press'
    values = {}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()  
    

print "Running dash2.py version 5"
print "Waiting for an amazon dash button to register to the network ..."

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()

  
# python 2.7  
# import urllib
# import urllib2

url = 'http://192.168.178.31:8083/fhem?cmd=set%20DashButton' + button + '%20press'
values = {}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()  

# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
# 
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# the_page = response.read()  


# eof  
