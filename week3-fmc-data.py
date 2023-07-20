import requests
import json
import pandas as pd

baseURL = "https://10.122.111.45/api/"

'open information text file'
f = open('week3-fmc-data-output.txt', "w")
f.write("FMC Device Health Overview \n \n")


'get access token for fmc'
try:
    authURL = "https://10.122.111.45/api/fmc_platform/v1/auth/generatetoken"
    auth = {
        'username': 'admin',
        'password':'Cisco.123',
        'token': '',
        'refresh': '',
        'cert': False
    }
    response = requests.post(url = authURL, auth =('admin','Cisco.123'), verify = False)
    authToken = response.headers['X-auth-access-token']
    domainUUID = response.headers['DOMAIN_UUID']
    print(response.status_code)
except:
    print("No auth")

print("^"*20)


'health alerts on fmc'
try:
    healthAlertURL = baseURL+ "fmc_config/v1/domain/" + domainUUID + "/health/alerts"
    healthParams = {'offset': '0', 'limit':'5'}
    healthHeaders = {'Content-Type': 'application/json', 'X-auth-access-token': authToken}
    healthResponse = requests.get(url = healthAlertURL, params= healthParams, headers= healthHeaders, verify = False)
    print(healthResponse.status_code)

    'format health info'
    dictResponse = json.loads(healthResponse.text)
    print(json.dumps(healthResponse.json(), indent=2))
    f = open('week3-fmc-data-output.txt', 'a')
    f.write('Health Alerts: \n')
    
    for key in dictResponse["items"]:
        f = open('week3-fmc-data-output.txt', 'a')
        f.write( key["moduleID"] + " status " + key['status'] + "\n")
except:
    print("failed")

print("*"*20)


'upgrade packages on FMC'
try:
    upgradeURL = baseURL + "fmc_platform/v1/updates/upgradepackages"
    upgradeParams= {'offset': '0', 'limit':'5'}
    upgradeHeaders = {'Content-Type': 'application/json', 'X-auth-access-token': authToken}
    upgradeResponse = requests.get(url = upgradeURL, params= upgradeParams, headers= upgradeHeaders, verify = False)
    print(upgradeResponse.status_code)

    'format upgrade info'
    upgradeDict = json.loads(upgradeResponse.text)
    usableInfo = []

    for item in upgradeDict["items"]:
        updgradeInfo = {
            "upgradeType": item["metadata"]["upgradeType"],
            "upgradeFile": item["metadata"]["upgradeFileName"]
        }
        usableInfo.append(updgradeInfo)

    df = pd.DataFrame(usableInfo)
    f = open('week3-fmc-data-output.txt', 'a')
    f.write("\nUpgrades: \n"+  df.to_string())
    print(json.dumps(upgradeResponse.json(), indent=2))
except:
    print("failed2")

print("&"*20)


'device records on FMC'
try:
    deviceRecordHeaders = {
        'Content-Type': 'application/json',
        'X-auth-access-token': authToken
    }
    DeviceRecordResponse = requests.get("https://10.122.111.45/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/devices/devicerecords", 
                        headers = deviceRecordHeaders,
                        params={'offset': '0', 'limit': '5'},
                        verify=auth['cert'])
    print(DeviceRecordResponse.status_code)

    'format device records'
    deviceDict = json.loads(DeviceRecordResponse.text)
    usefulInfo = []

    for item in deviceDict['items']:
        deviceInfo = {
            'deviceType': item['type'],
            'deviceName': item["name"]
        }
        usefulInfo.append(deviceInfo)
    
    deviceDF = pd.DataFrame(usefulInfo)
    f = open('week3-fmc-data-output.txt', 'a')
    f.write("\n \nDevice Records: \n" + deviceDF.to_string())
    print(json.dumps(DeviceRecordResponse.json(), indent=2))
except:
    print("failed3")
                        

f.close()

""" Mystery error code - find the error
try:
    deviceRecordURL = baseURL +'​fmc_config​/v1​/domain​/'+ domainUUID+ '​/devices​/devicerecords'
    print(deviceRecordURL)
    deviceRecordParams = {"offset": "0", "limit": "5"}
    deviceRecordHeaders = {'Content-Type': 'application/json', 'X-auth-access-token': authToken}
    deviceRecordsResponse = requests.get(url = deviceRecordURL, params= deviceRecordParams, headers= deviceRecordHeaders, verify = False)
    results +=  str(deviceRecordsResponse.status_code) + "\n"
    print(deviceRecordsResponse.status_code)
except:
    print("failed3")
print("%"*20)
"""
'Device records on FMC'