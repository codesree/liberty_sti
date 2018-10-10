import requests
import json
from requests.auth import HTTPBasicAuth



url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/sbsa/oauth/oauth2/token'

head = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json",
    'x-ibm-client-id':'3d67e856-8438-4ffa-a25e-b61058bc821c',
       }

payload = "grant_type=client_credentials&scope=quote"



user = '3d67e856-8438-4ffa-a25e-b61058bc821c'
passw = 'T6kC0mG0fW3xY1cD5kH3oF5wB0qW5fI7iQ8qF0lR2jO7wT7uM3'

authin = HTTPBasicAuth(username=user,password=passw)
response = requests.post(url,data=payload,headers=head,auth=authin)

print("Response  from API Gateway...........", response.status_code)

do_resp = response.json()
do_resp = json.dumps(do_resp, indent=5)

print(do_resp)
print(type(do_resp))


auth_token = do_resp['access_token']



