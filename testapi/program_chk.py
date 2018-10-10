
from pymongo import MongoClient
import requests

try:
    requests.get("http://sgfbjsm.com")


except(requests.exceptions.ConnectionError, requests.exceptions.Timeout):
    print("Error connecting to the Server..")
    resp = "Error connecting to the Server.."

# copy db from localhost to server
#db.copyDatabase('tag_users','tag_users','ds117423.mlab.com:17423',username='srekanth',password='liberty@123',authMechanism='SCRAM-SHA-1')


print("type..",type(resp))

datas = type(resp)


if type(resp) == str:
    print("String")