import datetime
import logging
import sys
import datetime
import time
import os



# Version for: home assistant / http post / state
def trigger_state(button):

  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  password = os.getenv('HB_HASSIO_API_PASSWORD', 'unknown')
  data     = """ '{{ "state": "on", "attributes": {{"button": "{}"}}  }}' """.format(button)
  
  
  
  # post tequest to /api/states/<entity_id> 
  # e.g. entity: sensor.dashbutton_caffe1
  url      = "http://hassio.internal:8123/api/states/sensor.dashbutton_{}".format(button)

  print "Making HTTP request for:", button
  print "p1: url = " + url

  curl(password, data, url)  


# Version for: home assistant / http post / event
def trigger_event(button):

  # The following environment variables are set by the 'docker run' command via the '--env-file' option
  password = os.getenv('HB_HASSIO_API_PASSWORD', 'unknown')
  data     = """ '{{ "state": true, "attributes": {{"button": "{}"}}  }}' """.format(button)
  url      = "http://hassio.internal:8123/api/events/button-pushed"

  print "Making HTTP request for:", button
  print "p1: url = " + url

  curl(password, data, url)  



def curl(password, data, url):
  cmd = """ curl -X POST -H "x-ha-access: {}" -H "Content-Type: application/json"  -d {} {} """.format(password, data, url)
  print "cmd = <<< " + cmd + " >>>"
  print ""
  print "The next line is the servers returned payload"
  result = os.system(cmd)
  print ""
  print "Result of OS command should be 0 and it is '" + str(result) + "'"
  print ""




trigger_state("ariel1")
#trigger_event("Caffee1")

# eof



