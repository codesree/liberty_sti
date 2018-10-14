
from pymongo import MongoClient
import requests
import os
# db = MongoClient('mongodb://ds117423.mlab.com:17423',
#                       username='srekanth',
#                       password='liberty@123',
#                       authSource='liberty_sti',
#                       authMechanism='SCRAM-SHA-1')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT=os.path.join(BASE_DIR, 'static/')

print(STATIC_ROOT)