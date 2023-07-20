import requests
import json

auth = {
'username': 'admin',
'password': 'Cisco.123',
'token': '',
'refresh': '',
'cert': False
}

path = "/api/fmc_config/v1/domain"

print(f"Getting access token from 10.122.111.45")
try:
    resp = requests.post(f"https://10.122.111.45/api/fmc_platform/v1/auth/generatetoken",
    auth =('admin','Cisco.123'),
    data={},
    verify=auth['cert'])
    auth['token'] = resp.headers['X-auth-access-token']
    auth['refresh_token'] = resp.headers['X-auth-refresh-token']
    path = path + "/" + resp.headers['DOMAIN_UUID']
    print("Token Received!")
except:
    print(f"Auth failed! {resp.status_code}")

try:
    my_headers = {
        'Content-Type': 'application/json',
        'X-auth-access-token': auth['token']
    }
    resp = requests.get("https://10.122.111.45/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords",
    headers=my_headers,
    params={'offset': '0', 'limit': '5'},
    verify=auth['cert'])
    if resp.status_code == 200:
        print(resp.json())
        print("="*10,"pretty printing", "="*10)
        print(json.dumps(resp.json(), indent=2))
    else:
        print(f"Failed with code: {resp.status_code}")
except:
    print("Python error!")