#!/usr/bin/env python3

import subprocess
from requests import post

# Get temperature from system
# Thermal Zone 1 is the first CPU. Update depending on CPU count.
temp=subprocess.check_output("cat /sys/class/thermal/thermal_zone1/temp", shell=True)

# Parse Temperature from given string
temp = [int(i) for i in temp.split() if i.isdigit()][0]
temp = temp * 0.001

# Replace hostname and port with your HA instance
# Make sure to use the correct protocol, http or https
url = "http://hostname:8123/api/states/input_number.cpu_temp"

# Replace ABCDEFG with your Long-lived access token
headers = {
  "Authorization": "Bearer ABCDEFG",
  "content-type": "application/json"
}

data = '{"state": %s}' % temp

response = post(url, headers=headers, data=data, verify=False)