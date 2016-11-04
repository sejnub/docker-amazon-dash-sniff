import datetime
import logging
import urllib
import urllib2

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def arp_display(pkt):
  if pkt.haslayer(ARP):
    if pkt[ARP].op == 1: #who-has (request)
      if pkt[ARP].hwsrc == 'ac:63:be:a3:5c:03': 
        button = "caffe-1"
      if pkt[ARP].hwsrc == 'ac:63:be:44:51:b3': 
        button = "ariel-1"
      if pkt[ARP].hwsrc == 'ac:63:be:e3:3c:64': 
        button = "somat-1"
      else:
        button = "unknown"
        
  if button == "unknown:
    print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
  else:
    print "Pushed button: " + button
    

print "Running dash2.py version 5"
print "Waiting for an amazon dash button to register to the network ..."

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()

  
# python 2.7  
# import urllib
# import urllib2

# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
# 
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# the_page = response.read()  


# eof  
