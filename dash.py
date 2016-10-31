import datetime
import logging
import urllib
import urllib2
 
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
def button_pressed_dash1():
  current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
  print 'Dash button somat-1 pressed at ' + current_time

def button_pressed_dash2():
  current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
  print 'Dash button ariel-1 pressed at ' + current_time
 
def button_pressed_dash3():
  current_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
  print 'Dash button caffe-1 pressed at ' + current_time
 
def udp_filter(pkt):
  options = pkt[DHCP].options
  for option in options:
    if isinstance(option, tuple):
     if 'requested_addr' in option:
       # we've found the IP address, which means its the second and final UDP request, so we can trigger our action
       mac_to_action[pkt.src]()
       break
 
mac_to_action = {'ac:63:be:e3:3c:64' : button_pressed_dash1, 
                 'ac:63:be:44:51:b3' : button_pressed_dash2, 
                 'ac:63:be:a3:5c:03' : button_pressed_dash3}
mac_id_list = list(mac_to_action.keys())
 
print "Running dash.py version 3"
print "Waiting for an amazon dash button to register to the network ..."

sniff(prn=udp_filter, store=0, filter="udp", lfilter=lambda d: d.src in mac_id_list)
 
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
