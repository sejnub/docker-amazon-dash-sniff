import datetime
import logging
import urllib
import urllib2

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].hwsrc == 'ac:63:be:a3:5c:0': # button 1
        print "Pushed Ariel"
    else:
        print "ARP Probe from unknown device: " + pkt[ARP].hwsrc


print "Running dash.py version 4"
print "Waiting for an amazon dash button to register to the network ..."

sniff(prn=arp_display, filter="arp", store=0, count=0)

if __name__ == "__main__":
  main()
