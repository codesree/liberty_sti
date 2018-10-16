from pymongo import MongoClient
import datetime
import json
import requests
import logging
import uuid,os
from oauthlib import oauth2
from requests.auth import HTTPBasicAuth



class Asset_stack():
    def __init__(self):
        global con
        db = MongoClient('mongodb://ds117423.mlab.com:17423',
                      username='srekanth',
                      password='liberty@123',
                      authSource='liberty_sti',
                      authMechanism='SCRAM-SHA-1')
        con = db['liberty_sti']

    def update_homecontent_item(self,rkey,rfact,rcount,tinfo):

        col = con['homecontent_items']
        ucount = 0
        print("Update started for home_content testcase.....")
        while ucount < rcount:
            if tinfo == "rate_enums":
                print('ucount:',ucount)
                for factnum in rfact.values():
                    if rkey == "discountType":
                        col.update({"itemType" : "HomeContent"},
                                   {'$set': {
                                       'discountDetails.discountType' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)

                    elif rkey == "policyFrequency":
                        col.update({"itemType" : "HomeContent"},
                                   {'$set': {
                                       'policyFrequency' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_homecontent_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    if rkey == "discountType":
                        col.update({"itemType": "HomeContent"},
                                   {'$set': {
                                       'discountDetails.discountType': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)

                    elif rkey == "policyFrequency":
                        col.update({"itemType": "HomeContent"},
                                   {'$set': {
                                       'policyFrequency': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_homecontent_item(ucount)
            ucount = ucount + 1

    def update_allrisks_item(self, rkey, rfact, rcount, tinfo):

        col = con['allrisks_item']
        ucount = 0
        print("Update started for AllRisks testcase.....")
        while ucount < rcount:
            if tinfo == "rate_enums":
                print('ucount:', ucount)
                for factnum in rfact.values():
                    if rkey == "discountType":
                        col.update({"itemType" : "AllRisk"},
                                   {'$set': {
                                       'discountDetails.discountType' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)

                    elif rkey == "policyFrequency":
                        col.update({"itemType" : "AllRisk"},
                                   {'$set': {
                                       'policyFrequency' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)

                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    if rkey == "discountType":
                        col.update({"itemType": "AllRisk"},
                                   {'$set': {
                                       'discountDetails.discountType': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)

                    elif rkey == "policyFrequency":
                        col.update({"itemType" : "AllRisk"},
                                   {'$set': {
                                       'policyFrequency' : factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
                    else:
                        col.update({'itemProperties.name': "" + rkey + ""},
                                   {'$set': {
                                       'itemProperties.$.value': factnum
                                   }
                                   }
                                   )
                        self.process_allrisks_item(ucount)
            ucount = ucount + 1

    def update_vehicle_item(self,rkey,rfact,rcount,tinfo):

        col = con['vehicle_item']
        print("rcount is..",rcount)
        ucount = 0
        while ucount < rcount:
            if tinfo == "rate_enums":
                for factnum in rfact.values():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': factnum
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': ""+factnum+""
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "cars":
                    card = rfact[ucount]
                    print("Build for",card['make'],"--",card['model'])
                    maked = card['make']
                    modeld = card['model']
                    yeard = card['year']
                    col.update({'itemProperties.name': "Make"},
                               {'$set': {
                                   'itemProperties.$.value': "" + maked + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Model"},
                               {'$set': {
                                   'itemProperties.$.value': "" + modeld + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Year"},
                               {'$set': {
                                   'itemProperties.$.value': "" + yeard + ""
                               }
                               }
                               )

                    self.process_vehicle_item(ucount)

            ucount = ucount + 1

    def update_personal_liability_item(self,rkey,rfact,rcount,tinfo):

        col = con['personal_liability_item']
        print("rcount is..",rcount)
        ucount = 0
        while ucount < rcount:
            if tinfo == "rate_enums":
                for factnum in rfact.values():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': factnum
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "rate_keys":
                for factnum in rfact.keys():
                    col.update({'itemProperties.name': "" + rkey + ""},
                               {'$set': {
                                   'itemProperties.$.value': ""+factnum+""
                               }
                               }
                               )
                    self.process_vehicle_item(ucount)
            elif tinfo == "cars":
                    card = rfact[ucount]
                    print("Build for",card['make'],"--",card['model'])
                    maked = card['make']
                    modeld = card['model']
                    yeard = card['year']
                    col.update({'itemProperties.name': "Make"},
                               {'$set': {
                                   'itemProperties.$.value': "" + maked + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Model"},
                               {'$set': {
                                   'itemProperties.$.value': "" + modeld + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Year"},
                               {'$set': {
                                   'itemProperties.$.value': "" + yeard + ""
                               }
                               }
                               )

                    self.process_vehicle_item(ucount)

            ucount = ucount + 1


    def build_asset_stack(self,stack_name):

        if stack_name == "Home_contents":
            col = con['homecontent_asset']
            asset_data = col.find_one({'name': 'Home Contents'})
        elif stack_name == "Motor_vehicles":
            col = con['vehicle_asset']
            asset_data = col.find_one({'name': 'Vehicles'})
        elif stack_name == "Building":
            col = con['vehicle_asset']
            asset_data = col.find_one({'name': 'Vehicles'})
        elif stack_name == "AllRisks":
            col = con['allrisks_asset']
            asset_data = col.find_one({'name': 'All Risks'})
        elif stack_name =="personal_liability":
            col = con['personal_liability_asset']
            asset_data = col.find_one({'name': 'Personal Liabilities'})

        del asset_data['_id']

        col = con['asset_api']

        col.update({'quoteHeader.srsId': 'SRS_ID'},
                   {'$set': {
                       'sections': []
                   }
                   }
                   )

        col.update({'quoteHeader.srsId': 'SRS_ID'},
                   {'$set': {
                       'sections.0': asset_data
                   }
                   }
                   )

        asset_req = col.find_one({"quoteHeader.srsId" : "SRS_ID"})

        del asset_req['_id']

        asset_req = json.dumps(asset_req, indent=5)
        return asset_req




    def process_homecontent_item(self,ucount):
        col = con['homecontent_items']
        build_item = col.find_one({"itemType":"HomeContent"})

        del build_item['_id']

        self.asset_content(build_item,ucount)


    def process_personal_liability_item(self,ucount):
        col = con['﻿=personal_liability_item']
        build_item = col.find_one({"itemType":"PersonalLiability"})

        del build_item['_id']

        self.asset_content(build_item,ucount)


    def process_vehicle_item(self,ucount):
        col = con['vehicle_item']
        build_item = col.find_one({'itemType': 'Vehicle'})

        del build_item['_id']

        self.asset_vehicle(build_item,ucount)

    def process_allrisks_item(self,ucount):
        col = con['allrisks_item']
        build_item = col.find_one({'itemType': 'AllRisk'})

        del build_item['_id']

        self.asset_allrisks(build_item,ucount)


    def asset_content(self,build_item,ucount):

        col = con['homecontent_asset']

        if ucount == 0:
            col.update({'name': 'Home Contents'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name': 'Home Contents'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )

    def asset_personal_liability(self,build_item,ucount):

        col = con['personal_liability_asset']

        if ucount == 0:
            col.update({'name': 'Personal Liabilities'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name': 'Personal Liabilities'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )

    def asset_allrisks(self,build_item,ucount):

        col = con['allrisks_asset']

        if ucount == 0:
            col.update({'name': 'All Risks'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name': 'All Risks'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )

    def asset_vehicle(self,build_item,ucount):

        col = con['vehicle_asset']

        if ucount == 0:
            col.update({'name':'Vehicles'},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )
        col.update({'name':'Vehicles'},
                   {
                       '$addToSet':
                           {
                               'items': build_item
                           }
                   }
                   )


class external_gateway_process():

    def __init__(self,func):
        global req_url,head,auth_tok
        funcp = func

        #gateway nonprod - oauth
        auth_tok = self.auth_token()
        oauthtok = 'Bearer '+ auth_tok

        head = {'Content-Type': 'application/json',
                'Accept': 'application/json',
                'authorization': oauthtok,
                'x-ibm-client-id': "3d67e856-8438-4ffa-a25e-b61058bc821c"
                }
        if funcp == "asset_api":
            #gateway non-prod:
            auth_tok = self.auth_token()
            req_url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/Process'
        elif funcp == "calculate_prorata":
            auth_tok = self.auth_token()
            req_url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/CalculateProRata'
        elif funcp == "convert_to_policy":
            auth_tok = self.auth_token()
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy//"
        elif funcp == "view_policy":
            auth_tok = self.auth_token()
            req_url = "http://prbk-pa001sap4v/Insurance.Quoting2/api/Policies/"





    def auth_token(self):

        url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/sbsa/oauth/oauth2/token'

        head = {
            'content-type': "application/x-www-form-urlencoded",
            'accept': "application/json",
            'x-ibm-client-id': '3d67e856-8438-4ffa-a25e-b61058bc821c',
        }

        payload = "grant_type=client_credentials&scope=quote"

        user = '3d67e856-8438-4ffa-a25e-b61058bc821c'
        passw = 'T6kC0mG0fW3xY1cD5kH3oF5wB0qW5fI7iQ8qF0lR2jO7wT7uM3'

        authin = HTTPBasicAuth(username=user, password=passw)
        response = requests.post(url, data=payload, headers=head, auth=authin)

        print("Response  from API Gateway...........", response.status_code)

        do_resp = response.json()
        auth_tok = do_resp['access_token']
        print(type(do_resp))


        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print(type(do_resp))

        return auth_tok

    def api_exec(self,api_req):

        do_req = api_req

        response = requests.post(req_url, data=do_req, headers=head)

        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp

    def convtop_exec(self,policy_n):
        req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy/"
        req_url = req_url + policy_n
        response = requests.post(req_url,headers=head)


        print("Response  from API Gateway...........", response.status_code)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp

    def view_policy(self,policy_n):
        vpolicy = policy_n

        vpolicy_url = req_url +policy_n
        response = requests.get(vpolicy_url,headers =head)
        do_resp = response.json()
        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print("Type of response data:", type(do_resp))
        return do_resp


class gateway_process():

    def __init__(self,func):
        global req_url,head
        funcp = func

        #gateway nonprod - oauth
        auth_tok = self.auth_token()
        oauthtok = 'Bearer '+ auth_tok

        head = {'Content-Type': 'application/json',
                'Accept': 'application/json',
                'authorization': oauthtok,
                'x-ibm-client-id': "3d67e856-8438-4ffa-a25e-b61058bc821c"
                }
        if funcp == "asset_api":
            #gateway non-prod:
            req_url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/Process'
        elif funcp == "calculate_prorata":
            req_url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/CalculateProRata'
        elif funcp == "convert_to_policy":
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy//"
        elif funcp == "view_policy":
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Policies/"
        elif funcp == "amend_quote":
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Quotes/"
        elif funcp == "process_policy":
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Policies/Process"
        elif funcp == "accept_policy":
            req_url = "https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/Insurance.Quoting2/api/Policies/AcceptPolicyAmendment/"

    def auth_token(self):

        url = 'https://gatewaynp.standardbank.co.za:5543/npextorg/extnonprod/sbsa/oauth/oauth2/token'

        head = {
            'content-type': "application/x-www-form-urlencoded",
            'accept': "application/json",
            'x-ibm-client-id': '3d67e856-8438-4ffa-a25e-b61058bc821c',
        }

        payload = "grant_type=client_credentials&scope=quote"

        user = '3d67e856-8438-4ffa-a25e-b61058bc821c'
        passw = 'T6kC0mG0fW3xY1cD5kH3oF5wB0qW5fI7iQ8qF0lR2jO7wT7uM3'

        authin = HTTPBasicAuth(username=user, password=passw)
        response = requests.post(url, data=payload, headers=head, auth=authin)

        print("Response  from API Gateway...........", response.status_code)

        do_resp = response.json()
        auth_tok = do_resp['access_token']
        print(type(do_resp))

        do_resp = json.dumps(do_resp, indent=5)

        print(do_resp)
        print(type(do_resp))

        return auth_tok

    def api_exec(self,api_req):


        do_req = api_req

        print(do_req)
        print(req_url)
        print(head)
        try:
            response = requests.post(req_url, data=do_req, headers=head)

            print("Response  from API Gateway...........", response.status_code)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp,statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp,statcode


    def convtop_exec(self,policy_n):

        req_url = "http://prbk-pa001sap4v/Insurance.Quoting2/api/Quotes/ConvertQuoteToPolicy/"
        req_url = req_url + policy_n

        try:
            response = requests.post(req_url, headers=head)

            print("Response  from API Gateway...........", response.status_code)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp, statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp, statcode


    def view_policy(self,policy_n):
        vpolicy = policy_n

        vpolicy_url = req_url +policy_n
        try:

            response = requests.get(vpolicy_url, headers=head)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp, statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp, statcode

    def view_quote(self,quote_n):
        vquote = quote_n

        vquote_url = req_url +vquote
        try:
            response = requests.get(vquote_url, headers=head)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp, statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp, statcode

    def process_policy(self,api_req):

        do_req = api_req

        print(req_url)
        print(head)
        try:
            response = requests.post(req_url, data=do_req, headers=head)

            print("Response  from API Gateway...........", response.status_code)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp,statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp,statcode

    def accept_policyendorse(self,policynum,decision):

        policynum = policynum

        if decision == "True":
            acdpol_url = req_url + policynum + "/true"
        elif decision == "False":
            acdpol_url = req_url + policynum + "/false"


        try:
            print(acdpol_url)
            response = requests.post(acdpol_url, headers=head)

            print("Response  from API Gateway...........", response.status_code)
            statcode = response.status_code
            do_resp = response.json()

            print(do_resp)
            print("Type of response data:", type(do_resp))
            return do_resp,statcode
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Connection time out....Server is down..')
            do_resp = "Connection timed out...SERVER IS DOWN !!..Please try again later."
            return do_resp,statcode


class test_rating_db(Asset_stack):

    def __init__(self,tconnect):
        global col,logger
        db = MongoClient('mongodb://ds117423.mlab.com:17423',
                      username='srekanth',
                      password='liberty@123',
                      authSource='liberty_sti',
                      authMechanism='SCRAM-SHA-1')
        con = db['liberty_sti']
        if tconnect == "rate_home_contents":
            col = con['rate_home_contents']
            print("Connected to --rate_home_contents--- test DB")
            glog = log_builder('Assetapi_homecontent')
            logger = glog.set_log('INFO', 'noformat')
        elif tconnect == 'rate_vehicles':
            col = con['rate_vehicles']
            print("Connected to --rate_vehicles--- test DB")
        elif tconnect == 'rate_allrisks':
            col = con['rate_allrisks']
            print("Connected to --rate_allrisks--- test DB")


    def get_rating_factors(self,caseval,testcase,tinfo):

        global precount

        if testcase == "asset_homecontent":
            tab_title = "rate_contents"
        elif testcase == "asset_vehicle":
            tab_title = "rate_vehicles"
        elif testcase == "asset_allrisks":
            tab_title = "rate_allrisks"

        rtcont = col.find_one({"title": "" + tab_title + ""})

        del rtcont['_id']
        rcfact = rtcont['ratingfactors']
        datak = rcfact.keys()
        print(datak)
        datal = list(datak)
        kcount = 0
        while kcount < len(datal):
            print("key count is", kcount)
            if datal[kcount] == caseval:
                print("found!!!!")
                print(datal[kcount])

                testkey = datal[kcount]

                print(rcfact[testkey])
                logger.info(rcfact[testkey])
                testfact = rcfact[testkey]
                precount = len(testfact)

                print(precount)

                """Process the request json in mongodb using
                   1.testkey  - datatype - char (eg: "ControlledAccess")
                   2.testfact - datatype - dict (eg:{"key":"value".....}) 
                   3.precount - datatype - int  (eg: total number for updates to perform and add)
                """
                break
            kcount = kcount + 1
        else:
            print("Test_Rating_factor Key does not exist in test DB..Test case failed")

        assetops = Asset_stack()

        if tab_title == "rate_contents":
            assetops.update_homecontent_item(testkey, testfact, precount,tinfo)

        if tab_title == "rate_vehicles":
            assetops.update_vehicle_item(testkey, testfact, precount,tinfo)

        if tab_title == "rate_allrisks":
            assetops.update_allrisks_item(testkey,testfact,precount,tinfo)


class All_safe(test_rating_db):
    def __init__(self):
        pass

    def test_all_safe(self,saftyp,cont):

        global logfil,report_file,amend_quote,quote_n,policy_n,policy_detail

        print('Entering AllSafe - chamber....')

        if saftyp == 'file':
            logfil = cont
        elif saftyp == 'report':
            report_file = cont
        elif saftyp == "getfile":
            return logfil
        elif saftyp == "getreport":
            return report_file
        elif saftyp == "amend_quote":
            amend_quote = cont
        elif saftyp == "get_amend_quote":
            print("get amend quote...",amend_quote)
            return amend_quote
        elif saftyp == "quote_no":
            quote_n = cont
            print("quote number logged..",quote_n)
        elif saftyp == "get_quote_n":
            return quote_n
        elif saftyp == "policy_no":
            policy_n = cont
        elif saftyp == "get_policy_n":
            return policy_n
        elif saftyp == "policy_detail":
            policy_detail = cont
        elif saftyp == "get_policy_detail":
            return policy_detail



    def checkoutput(self,asset_resp):

        asset_resp = asset_resp[0]

        #asset_resp = json.loads(asset_resp)
        ikey = precount
        itemp = asset_resp['items']

        print("item_key expected: ",ikey)
        print("item_key from response: ", itemp)

        """
        print('counter is',ikey)
        print('asset response length is..',len(storesp))

        quotn = storesp['quoteNumber']
        print('quote number is..',quotn)
        itemp = storesp['items']

        print('length of item premium..',len(itemp))
        """
        try:
            assert len(asset_resp) > 1

            assert asset_resp['quoteNumber']
            quotn = asset_resp['quoteNumber']
            assert len(quotn) > 5

            itemp = asset_resp['items']


            assert len(itemp) == ikey

            print("am PASS")
            return 'PASS'

        except:
            return 'FAIL'

        finally:

            print('api response - validation completed...')


class report_builder():

    def __init__(self, logsuit):
        global logcol, unid

        logdb = MongoClient()
        logcon = logdb['test_data']
        logcol = logcon['test_report']

        if logsuit != 'handover':

            if logsuit == 'asset_homecontent':
                test_suite = '﻿Home contents Rating Factors - Asset API'
            elif logsuit == 'asset_vehicle':
                test_suite = 'Vehicles Rating Factors - Asset API'
            elif logsuit == 'asset_allrisks':
                test_suite = 'AllRisks Rating Factors - Asset API'
            elif logsuit == 'quote_to_policy':
                test_suite = 'Process Quote - Asset API'

            unid = uuid.uuid4()
            unid = str(unid)
            logcol.insert({
                '_id': '' + unid + '',
                'test_suite': '' + logsuit + ''
            })
        else:
            pass

    def log_repdata(self, logdat, logres):

        if logres == 'testsuite':
            tcdat = logdat['testc']
            logcol.update({
                '_id': '' + unid + ''
            },
                {
                    '$set': {
                        'test_cases': tcdat,
                        'time_taken': logdat['time_taken'],
                        'start_time': logdat['start_time'],
                        'end_time': logdat['end_time']
                    }
                }
            )

    def report_handover(self, func):
        trept = logcol.find_one({'_id': '' + unid + ''})
        if func == 'handover':
            print("handover initiated....")
            gs = All_safe()
            gs.test_all_safe('report', trept)


class log_builder():

    def __init__(self, logfile):

        global tfilename, logapi, chin

        logapi = logfile
        curr_time = datetime.datetime.now().isoformat()
        if logfile == 'Assetapi_homecontent':
            tfilename = 'log_asset_homecont_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'
        elif logfile == 'asset_vehicle':
            tfilename = 'log_asset_vehicle_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'quote_to_policy':
            tfilename = 'log_process_quote_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'asset_allrisks':
            tfilename = 'log_asset_allrisks_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'asset_api':
            tfilename = 'create_quote_log_'+ curr_time
            tfilename = tfilename + '.json'

        elif logfile == 'policy_api':
            tfilename = 'amend_policy_log_'+ curr_time
            tfilename = tfilename + '.json'

        elif logfile == 'accept_policy':
            tfilename = 'accept_policy_log_'+ curr_time
            tfilename = tfilename + '.json'

        elif logfile == 'asset_api_calcpror':
            tfilename = 'calc_prorata_log_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        elif logfile == 'asset_api_conv_to_policy_':
            tfilename = 'conv_to_policy_' + curr_time
            print(tfilename)
            tfilename = tfilename + '.json'

        dir = os.path.join('testapi/test_chamber')
        chin = logging.FileHandler(os.path.join(dir, tfilename), "a")

    def return_file(self):
        print(tfilename)
        return tfilename

    def set_log(self, loglevl, format):

        if format == 'format':
            format = '%(levelname)s - %(name)s - %(message)s - %(asctime)s'
        elif format == 'noformat':
            format = ''

        global logger
        logger = logging.getLogger(logapi)
        if loglevl == 'DEBUG':
            logger.setLevel(logging.DEBUG)
            chin.setLevel(logging.DEBUG)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'INFO':
            logger.setLevel(logging.INFO)
            chin.setLevel(logging.INFO)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'WARNING':
            logger.setLevel(logging.WARNING)
            chin.setLevel(logging.WARNING)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger
        elif loglevl == 'ERROR':
            logger.setLevel(logging.ERROR)
            chin.setLevel(logging.ERROR)
            formatter = logging.Formatter(format)
            chin.setFormatter(formatter)
            logger.addHandler(chin)
            return logger

    def file_handover(self, func):
        if func == 'handover':
            gs = All_safe()
            gs.test_all_safe('file', tfilename)


class Rating_engine():

    def __init__(self):
        pass

    def rating_trap(self,rpath, rfile):

        rmpath = rpath

        list_of_files = os.listdir(rmpath)
        # print(list_of_files)
        each_file = list_of_files

        rreqf = os.path.join(rmpath,rfile)

        try:
            os.path.exists(rreqf)

            for file in each_file:

                if file.startswith(rfile):

                    print("found!!!")
                    rreqf = os.path.join(rmpath, file)
                    print(rreqf)
                    rreqf = f"'{rreqf}'"
                    print(rreqf)
                    dreqf = dirn
                    dreqf = f"'{dreqf}'"

                    cmder = 'cp -av ' + rreqf + ' ' + dreqf
                    print(cmder)
                    os.popen(cmder)
        except:
            pass

    def direct_log(self,quote_n):
        global dirn
        try:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            print(BASE_DIR)
            LOG_DIR = os.path.join(BASE_DIR, "testapi/Log_data/")
            dirn = LOG_DIR + quote_n
            os.mkdir(dirn)

            return dirn

        except FileExistsError:
            print("Directory already exist!!!")
            pass


class Policy_api():
    def __init__(self,spinner):
        global col
        if spinner == 'get_policy' or spinner == 'log_policy' or spinner == 'amend_policy':
            db = MongoClient('mongodb://ds117423.mlab.com:17423',
                             username='srekanth',
                             password='liberty@123',
                             authSource='liberty_sti',
                             authMechanism='SCRAM-SHA-1')
            con = db['liberty_sti']
            col = con['policy_hub']
            print('connected to Policy_hub now........')
        elif spinner == "acdec_amend":
            db = MongoClient()
            con = db['testman']
            col = con['accept_policy_amendment']
            print('connected to accept_policy_amendment now........')


    def policy_base(self):
        self.pldata = col.find({})
        self.policy_list = []
        for doc in self.pldata:
            del doc['created_quote']
            del doc['_id']
            self.policy_list.append(doc)
        return self.policy_list


    def policy_log(self, userid, policy_number, quotes):
        time_stamp = datetime.datetime.now().isoformat()
        self.puser = userid
        self.policy_number = policy_number
        self.quotes = quotes
        status = 'active'
        col.insert(
            {
                "policy_number": self.policy_number,
                "created_by": self.puser,
                "created_on": time_stamp,
                "status": status,
                "created_quote": self.quotes

            })
        print("Log operation completed.....")








"""
if __name__ == '__main__':
    print("main")

    assetops = Homecontent_asset()
    #assetops.update_homecontent_item()
    assetops.process_homecontent_item()

    #contfact = test_rating_db()
    #contfact.get_rating_factors("home_contents")
    
"""