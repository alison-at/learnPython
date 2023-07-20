import requests

apiUrl = "https://webexapis.com/v1/people"
access_token = 'NDg2YmEyYmUtODRiYS00MDM5LTllNmItMWJhYzE3NmU4YWE2M2EyNDIxOGQtYTdk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
httpHeaders = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}
queryParams = {'displayName': 'Alison', 'max': '2'}

response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams)
print(response.status_code)
print("-"*20)
print(response.text)
print("-"*20)
print(response.json())

