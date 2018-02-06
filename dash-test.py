import datetime
import logging
#import urllib
#import urllib2
import sys
#import base64
import datetime
import time
import os


urlbase  = "http://hassio.internal:8123/api/events/button_pushed"
password = "password"

# Make an HTTP get request
def trigger(button):
  dashbutton = button # This line was meant to give button a prefix like "dash_".
  print "Making HTTP request for:", dashbutton

  url = urlbase # + dashbutton
  print "p1: url = " + url

  data = """ '{"state": """ + """ true """ + """ , "attributes": """ + \
         """   {"button": \"""" + dashbutton + """\"} """    + \
         """ }' """


  cmd = """ curl -X POST -H "x-ha-access: """ + password + '"' +  """ -H "Content-Type: application/json"  -d """ + data + " " + url
  

  print "cmd = <<< " + cmd + " >>>"


  result = os.system(cmd)

  print ""
  print "result should be 0 and it is '" + str(result) + "'"
  print ""


trigger("Caffee1")

# eof
