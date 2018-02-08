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

  data1 = """ '{{ "state": true, "attributes": {{"button": "{}"}}  }}' """
  print "data1 = <<< " + data1 + " >>>"
  data2 = data1.format("true")
  print "data2 = <<< " + data2 + " >>>"
  cmd1  = """ curl -X POST -H "x-ha-access: {}" -H "Content-Type: application/json"  -d {} {} """
  print "cmd1 = <<< " + cmd1 + " >>>"
  cmd2  = cmd1.format(password, data2, url)
  print "cmd2 = <<< " + cmd2 + " >>>"

  cmd = """ curl -X POST -H "x-ha-access: """ + password + '"' +  """ -H "Content-Type: application/json"  -d """ + data + " " + url

  print "cmd = <<< " + cmd + " >>>"

  print "The next line is the servers returned payload"
  result = os.system(cmd)
  print ""
  print "Result of OS command should be 0 and it is '" + str(result) + "'"
  print ""


trigger("Caffee1")

# eof



