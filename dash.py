import datetime
import logging
import urllib
import urllib2
import sys
import base64


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def arp_display(pkt):
  button = 'no-arp-op-1'
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: #who-has (request)
      
      elif pkt[ARP].hwsrc == 'ac:63:be:44:51:b3': 
        button = 'Ariel1'
        
      elif pkt[ARP].hwsrc == 'ac:63:be:1f:e7:fd': 
        button = 'Bio1'
      
      elif pkt[ARP].hwsrc == '50:f5:da:07:64:71': 
        button = 'Bio2'
      
      if   pkt[ARP].hwsrc == 'ac:63:be:a3:5c:03': 
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
  else:
    print " "
    print "Pushed button: " + button 
    
    username = "<username>"
    password = "<password>"
    url = '<some url that contains the button variable>'
    request = urllib2.Request(url)
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    response = urllib2.urlopen(request)    
    the_page = response.read()  
    

print "Running dash2.py version 5"
print "Waiting for an amazon dash button to register to the network ..."

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()

# eof  
