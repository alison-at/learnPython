import requests

access_Token = '2799c82e-e2d3-433e-9ea5-0c4923e95e25'
apiUrl = "https://10.122.111.45/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/users/authroles"
"'https://10.122.111.45/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords'"
httpHeaders = {'Content-Type': 'application/json', 'X-auth-access-token':  access_Token}
queryParams = {'expanded': 'false', 'offset': 0, 'limit': 2}

response = requests.get(url = apiUrl, headers = httpHeaders, params= queryParams, verify = False)
print(response.status_code)
print('&'*20)
print(response.json())

