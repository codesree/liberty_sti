from pymongo import MongoClient
import datetime
import json


class asset_manager():

    def __init__(self):

        global con
        db = MongoClient('mongodb://ds117423.mlab.com:17423',
                      username='srekanth',
                      password='liberty@123',
                      authSource='liberty_sti',
                      authMechanism='SCRAM-SHA-1')
        con = db['liberty_sti']


    def calculate_prorata(self,quoten):
        print(quoten)

        col = con['calculate_prorata']

        col.update({"referralOverrideIndicator":True},
                              {'$set':{
                                  "quoteNumber": ""+quoten+""
                              }
                              })
        accept_q = col.find_one({"quoteNumber": ""+quoten+""})
        print(accept_q['quoteNumber'])
        print(quoten)

        try:
            assert accept_q['quoteNumber'] == quoten
            del accept_q['_id']
            accept_q = json.dumps(accept_q, indent=5)
            return accept_q
        except:
            print('error in processing calculate prorata quote')
            return accept_q


    def process_carlist(self):

        col = con['rate_vehicles']

        vehid = col.find_one({"title": "rate_vehicles"})

        carsd = vehid['ratingfactors']['CARS']


        return carsd

    def get_vehicles(self,doman,vdata):

        col = con['rate_vehicles']


        try:
            assert doman == 'get_vehicle' and vdata is not []

            vehid = col.find_one({"title": "rate_vehicles"})

            carsd = vehid['ratingfactors']['CARS']

            ulist = vdata
            print(len(ulist))

            try:
                assert len(ulist) >= 1
                motor_ul = []
                ui = 0
                for ui in ulist:
                    for cl in carsd:
                        if cl['model'] == ui:
                            motor_ul.append(cl)
                print("List:", motor_ul)
                return motor_ul
            except:
                print("error at try block")
                for cl in carsd:
                    if cl['model'] == ulist[0]:
                        print("found!!", cl)
                        return cl

        except:
            print("No Vehicles selected by the user")
            emp = []
            return emp



    def asset_composer(self,asset_dict):


        asset_secl = []

        # Build Motor_vehicle
        print(asset_dict['motor_list'])
        try:
            assert len(asset_dict['motor_list']) != 0
            motordl = asset_dict['motor_list']
            mtrdlen = len(motordl)
            asset_m = self.build_asset('motor_vehicle',motordl,mtrdlen)

            asset_secl.append(asset_m)
        except:
            print('no update scheduled for motor vehicles')

        # Build Home_contents
        print(asset_dict['content_list'])

        try:
            assert len(asset_dict['content_list']) != 0
            contndl = asset_dict['content_list']
            cntdlen = len(contndl)
            asset_c = self.build_asset('home_content',contndl,cntdlen)

            asset_secl.append(asset_c)
        except:
            print('no update scheduled for Home Content')

        # Build All_risks
        print(asset_dict['allrisk_list'])

        try:
            assert len(asset_dict['allrisk_list']) != 0
            print("allrisk update processing ....")
            allrkdl = asset_dict['allrisk_list']
            alrdlen = len(allrkdl)
            asset_a = self.build_asset('allrisks',allrkdl,alrdlen)

            asset_secl.append(asset_a)

        except:
            print('no update scheduled for All risks')


        # Build Buildings
        print(asset_dict['building_list'])

        try:
            assert len(asset_dict['building_list']) != 0
            print("building update processing ....")
            builddl = asset_dict['building_list']
            buldlen = len(allrkdl)
            asset_b = self.build_asset('building',builddl,buldlen)

            asset_secl.append(asset_b)

        except:
            print('no update scheduled for Buildings')

        # Build Personal liabilities
        print(asset_dict['persliab_list'])

        try:
            assert len(asset_dict['persliab_list']) != 0
            print("building update processing ....")
            persldl = asset_dict['persliab_list']
            perllen = len(allrkdl)
            asset_p = self.build_asset('persliab',persldl,perllen)

            asset_secl.append(asset_p)

        except:
            print('no update scheduled for Buildings')

        # Build Sections - DESTINY

        try:
            assert asset_secl is not []
            asset_req = self.asset_comb(asset_secl,'SRS_ID')

            return asset_req

        except:
            print("Unable to retrieve asset api request...some processing error might have occured..")


    def build_asset(self,collect,iteml,updcount):

        try:
            assert collect == 'motor_vehicle'
            col = con['vehicle_item_draft']
            chkc = 0
            while chkc < updcount:
                for md in iteml:
                    col.update({'itemProperties.name': "Make"},
                               {'$set': {
                                   'itemProperties.$.value': "" + md['make'] + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Model"},
                               {'$set': {
                                   'itemProperties.$.value': "" + md['model'] + ""
                               }
                               }
                               )
                    col.update({'itemProperties.name': "Year"},
                               {'$set': {
                                   'itemProperties.$.value': "" + md['year'] + ""
                               }
                               }
                               )
                    col.update({'itemType':'Vehicle'},
                               {'$set':{
                                   'itemKey':''+md['model']+''
                               }})
                    self.asset_stack('vehicle_item_draft', 'vehicle_asset', 'Vehicles', 'Vehicle', chkc)
                    chkc = chkc + 1


            motor_pro = self.asset_strip('vehicle_asset','Vehicles')

            return motor_pro

        except:
            print("Build motor bypassed.......")


        try:
            assert collect == 'home_content'
            col = con['homecontent_item_draft']
            chkc = 0
            while chkc < updcount:
                for hd in iteml:
                    col.update({'itemType': "HomeContent"},
                               {'$set': {
                                   'name': '' + hd + '',
                                   'itemKey': '' + hd + ''
                               }
                               }
                               )
                    self.asset_stack('homecontent_item_draft','homecontent_asset', 'Home Contents','HomeContent', chkc)
                    chkc = chkc + 1

            homec_pro = self.asset_strip('homecontent_asset', 'Home Contents')
            print("build homecontent completed")
            return homec_pro

        except:
            print("build homecontent bypassed......")


        try:
            assert collect == 'allrisks'
            col = con['allrisks_item_draft']
            chkc = 0
            while chkc < updcount:
                for ad in iteml:
                    col.update({'itemType': "AllRisk"},
                               {'$set': {
                                   'name': '' + ad + '',
                                   'itemKey': '' + ad + ''
                               }
                               }
                               )

                    self.asset_stack('allrisks_item_draft', 'allrisks_asset', 'All Risks', 'AllRisk', chkc)
                    chkc = chkc + 1

            allrisk_pro = self.asset_strip('allrisks_asset', 'All Risks')
            print("build allrisks completed")


            return allrisk_pro

        except:
            print("build allrisk bypassed.......")

        try:
            assert collect == 'persliab'
            col = con['﻿personal_liability_item_draft']
            chkc = 0
            while chkc < updcount:
                for ad in iteml:
                    col.update({'itemType': "PersonalLiability"},
                               {'$set': {
                                   'name': '' + ad + '',
                                   'itemKey': '' + ad + ''
                               }
                               }
                               )

                    self.asset_stack('personal_liability_item_draft', 'personal_liability_asset', 'Personal Liabilities', '﻿PersonalLiability', chkc)
                    chkc = chkc + 1

            persliab_pro = self.asset_strip('personal_liability_asset', 'Personal Liabilities')
            print("build persliab completed")


            return persliab_pro

        except:
            print("build allrisk bypassed.......")

        try:
            assert collect == 'building'
            col = con['﻿building_item_draft']
            chkc = 0
            while chkc < updcount:
                for ad in iteml:
                    col.update({'itemType': "Building"},
                               {'$set': {
                                   'name': '' + ad + '',
                                   'itemKey': '' + ad + ''
                               }
                               }
                               )

                    self.asset_stack('﻿building_item_draft', '﻿building_asset', 'building', '﻿personal_liability', chkc)
                    chkc = chkc + 1

            allrisk_pro = self.asset_strip('allrisks_asset', 'All Risks')
            print("build allrisks completed")


            return allrisk_pro

        except:
            print("build allrisk bypassed.......")







    def asset_stack(self,load_item,load_asset,load_assetn,load_itemn,updc):

        col =con[load_item]
        asset_item = col.find_one({'itemType':load_itemn})
        del asset_item['_id']

        col =con[load_asset]

        if updc == 0:
            col.update({'name': load_assetn},
                       {
                           '$set':
                               {
                                   'items':[]
                               }
                       }
                       )

        col.update({'name':load_assetn },
                   {
                       '$addToSet':
                           {
                               'items': asset_item
                           }
                   }
                   )

    def asset_strip(self,collect,assetn):

        col = con[collect]
        asset_data = col.find_one({'name':assetn})

        del asset_data['_id']
        return asset_data



    def asset_comb(self,assetsec,assetn):
        col = con['asset_api']

        col.update({'quoteHeader.srsId':assetn},
                   {'$set': {
                       'sections': assetsec
                   }
                   }
                   )

        asset_req = col.find_one({"quoteHeader.srsId":assetn})

        del asset_req['_id']

        asset_req = json.dumps(asset_req, indent=5)
        return asset_req


    def loader(self):
        time_stamp = datetime.datetime.now().isoformat()
        userid = 'c2408856'
        policy_number = 'SHL000001258'
        status = 'active'
        col.insert(
            {
                "policy_number": policy_number,
                "created_by": userid,
                "created_on": time_stamp,
                "status": status
            }
        )

    def updater(self):
        time_stamp = datetime.datetime.now().isoformat()
        userid = 'c2408873'
        policy_number = 'SHL000001234'
        status = 'active'
        col.update(
            {
                "policy_number": "SHL000001234",
            },
            {
                "$set":
                    {
                        "created_quote": "QUOTE data"
                    }
            })

    def perform(self):
        podata = col.find()
        lister = []
        for doc in podata:
            print(type(doc))
            print(doc)
            del doc['created_quote']
            del doc['_id']
            lister.append(doc)

        print(type(podata))
        print(podata)
        print(lister)

    def amendpro(self,selp):
        self.policy = selp
        qcur = col.find_one({"policy_number": self.policy})

        self.qdata = qcur['created_quote']
        #print('quote :', self.qdata)
        self.qdata = json.loads(self.qdata)


        col.update(
            {
                "policy_number":self.policy},
                   {"$set":
                         {
                             "amend_quote":self.qdata
                         }
                   })
        self.perform_tokens()
        print("type of upd token",type(upd_token))
        print("Update token",upd_token)
        col.update({
            "policy_number":self.policy
        },
            {
                "$set":upd_token
            }
        )
        acur = col.find_one({"policy_number": self.policy})

        self.amdata = acur['amend_quote']
        self.amdata = json.dumps(self.amdata, indent=5)

        return self.amdata

    def perform_tokens(self):
        global upd_token
        upd_token = {}
        toPersons = {
            "amend_quote.Persons.0.State": "POLICY",
            "amend_quote.Persons.0.Status": "ACTIVE",
            "amend_quote.Persons.0.ActionType": "U"
        }
        upd_token.update(toPersons)
        toVehicle = {
            "amend_quote.QuoteDetails.Vehicle.0.State": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0.Status": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0.ActionType": "U"
        }
        upd_token.update(toVehicle)
        toMotorAccessories = {
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.State": "POLICY",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.Status": "ACTIVE",
            "amend_quote.QuoteDetails.Vehicle.0.MotorAccessories.0.ActionType": "U"
        }
        upd_token.update(toMotorAccessories)
        toDrivers = {
            "amend_quote.Persons.0.DriverTests.0.State": "POLICY",
            "amend_quote.Persons.0.DriverTests.0.Status": "ACTIVE",
            "amend_quote.Persons.0.DriverTests.0.ActionType": "U"
        }
        upd_token.update(toDrivers)
        toITCDetails = {
            "amend_quote.ITCDetails.State": "POLICY",
            "amend_quote.ITCDetails.Status": "ACTIVE",
            "amend_quote.ITCDetails.ActionType": "U"
        }
        upd_token.update(toITCDetails)
        toContacts = {
            "amend_quote.Contacts.0.State": "POLICY",
            "amend_quote.Contacts.0.Status": "ACTIVE",
            "amend_quote.Contacts.0.ActionType": "U"
        }
        upd_token.update(toContacts)
        toBankingDetails = {
            "amend_quote.BankingDetails.0.State": "POLICY",
            "amend_quote.BankingDetails.0.Status": "ACTIVE",
            "amend_quote.BankingDetails.0.ActionType": "U"
        }
        upd_token.update(toBankingDetails)
        toAddressses = {
            "amend_quote.Addressses.0.State": "POLICY",
            "amend_quote.Addressses.0.Status": "ACTIVE",
            "amend_quote.Addressses.0.ActionType": "U"
        }
        upd_token.update(toAddressses)

    def asset_operation(self,motor,building,home,stacker):

        self.motor = motor
        self.building = building
        self.home = home
        self.stacker = stacker

        if self.motor != 'ok':
            col = con['vehicle_item_draft']
            motor_item = col.find_one({'name': 'Vehicle'})
            print(type(motor_item))
            del motor_item['_id']

            col = con['vehicle_asset']

            col.update({'name': 'Vehicles'},
                       {'$set': {
                           'items.0': motor_item
                       }
                       }
                       )
        elif self.building != 'ok':
            col = con['building_item']
            build_item = col.find_one({'name': 'Buildings'})

            del build_item['_id']

            col = con['building_asset']
            col.update({'name': 'Buildings'},
                       {'$set': {
                           'items.0': build_item
                       }
                       }
                       )


        elif self.home != 'ok':
            col = con['homecontent_item_draft']
            build_item = col.find_one({'name': 'HomeContent'})
            del build_item['_id']

            col = con['homecontent_asset']
            col.update({'name': 'HomeContents'},
                       {'$set': {
                           'items.0': build_item
                       }
                       }
                       )


        elif self.stacker == 'do':
            asset_stack = self.get_asset_stack()
            col = con['asset_api']
            print(motor_as)
            col.update({'quoteHeader.srsId': 'SRS_ID'},
                       {'$set': {
                           'sections': asset_stack

                       }
                       }
                       )


    def get_asset_stack(self):

        col = con['vehicle_asset']

        asset_stack = []

        global motor_as

        motor_as = col.find_one({'name': 'Vehicles'})
        del motor_as['_id']
        asset_stack.append(motor_as)

        global build_as
        col = con['building_asset']
        build_as = col.find_one({'name': 'Buildings'})
        del build_as['_id']
        asset_stack.append(build_as)

        global home_as
        col = con['homecontent_asset']
        home_as = col.find_one({'name': 'HomeContents'})
        del home_as['_id']
        asset_stack.append(home_as)

        return asset_stack


class Asset_endtoend():

    def __init__(self):
        pass


    def create_quote(self):
        motord = [{'make': 'FORD', 'model': 'MUSTANG 2.3 ECOBOOST', 'year': '2016'}]
        content_sel = ['Refrigerator']
        allrisk_sel = ['Jewellery']


        asset_dict = {
            'motor_list': motord,
            'content_list': content_sel,
            'allrisk_list': allrisk_sel
        }

        aops = asset_manager()
        asset_api_req = aops.asset_composer(asset_dict)

        return asset_api_req

    def create_quote_check(self,asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200:
            #print("quote number", aquotn)
            #print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def view_quote_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def calculate_prorata(self,quote_n):

        quote_n =quote_n
        calcp = asset_manager()
        calcp_req = calcp.calculate_prorata(quote_n)

        return calcp_req

    def calculate_prorata_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def convtopol_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def view_policy_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def amendpolicy_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'

    def acdpol_check(self, asset_resp):

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        if asset_respcode == 200 :
            print("Am Pass!!")

            return 'PASS'

        else:
            print("Am Fail!!")
            return 'FAIL'



if __name__ == '__main__':

    dbops = asset_manager()

    my_op = "calculate_prorata"

    if my_op == "update":
        dbops.updater()
    elif my_op == "insert":
        print('am doing an insertion')
        dbops.loader()
    elif my_op == "perform":
        print("processing....")
        dbops.perform()
    elif my_op == "amend":
        policyn = "SHL000003115"
        dbops.amendpro(policyn)
    elif my_op =='asset':
        motor = 'ok'
        building = 'ok'
        home = 'ok'
        stacker = 'do'
        dbops.asset_manager(motor,building,home,stacker)
    elif my_op == 'calculate_prorata':
        dbops.calculate_prorata('SHL000011552')










