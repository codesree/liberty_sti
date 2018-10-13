from django.shortcuts import render
import json,time
from .mprocess import Monprocess
from .nprocess import Policy_starter
import requests
from .offline_composer import Composer

import os
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from .tests import asset_homecontent,asset_vehicle,asset_allrisks,report_builder,log_builder,asset_api_process
from .test_gate import All_safe,gateway_process,Rating_engine,Policy_api
from .test_chamber.testunit import awscert

import unittest
import zipfile,shutil
from io import StringIO

from django.urls import resolvers,reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import Userform
from .asset_manager import asset_manager


def index(request):
    context_dict = {'text': 'TAG - DASHBOARD'}
    return render(request, 'tag_home.html', context_dict)

def test_chamber(request):
    return render(request,'test_chamber_home.html')


def test_suite_home(request):
    return render(request,'asset_test_suite.html')

def asset_end_to_end_home(request):
    return render(request,'asset_api_flow.html')

def asset_homecon_suite(request):

    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_homecontent))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')
    return render(request, 'asset_test_suite.html', {
        'tstat': 'hcdone',
        'logfile': logfil,
        'testrep': treprt
    })


def asset_vehicle_suite(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_vehicle))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')

    return render(request, 'asset_test_suite.html', {
        'tstat': 'mvdone',
        'logfile': logfil,
        'testrep': treprt
    })


def asset_end_to_end(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_api_process))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')

    return render(request, 'asset_api_flow.html', {
        'tstat': 'assetdone',
        'logfile': logfil,
        'testrep': treprt
    })

def asset_allrisk_suite(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_allrisks))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')
    print('test report:',treprt)
    return render(request, 'asset_test_suite.html', {
        'tstat': 'ardone',
        'logfile': logfil,
        'testrep': treprt
    })


def asset_personal_liability_suite(request):
    tcrun = unittest.TextTestRunner()

    global logfil, treprt
    logfil = 0
    treprt = 0
    # tcrun = HTMLTestRunner(output='/Users/isree/PycharmProjects/tag-build/api_tag/templates/', template='', )
    # runner = HTMLTestRunner(output='example_suite')
    tcrun.run(unittest.makeSuite(asset_personal_liability_suite))
    gs = All_safe()
    logfil = gs.test_all_safe('getfile', 'test')
    treprt = gs.test_all_safe('getreport', 'test')
    print('test report:',treprt)
    return render(request, 'asset_test_suite.html', {
        'tstat': 'pldone',
        'logfile': logfil,
        'testrep': treprt
    })


def startp(request):
    return render(request,"test_loader.html")


def test_load(request):
    time.sleep(5)

    print('hello')

    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    print(fname)
    print(lname)

    time.sleep(5)


    return render(request,"test_loader.html")


def test_report(request):

    print(treprt)
    tname = treprt['test_suite']
    tcase = treprt['test_cases']
    ttake = treprt['time_taken']
    tstrt = treprt['start_time']
    tendt = treprt['end_time']

    texe = 0
    tpas = 0
    tfal = 0

    for td in tcase:
        texe = texe + 1
        if td['status'] == 'PASS':
            tpas = tpas + 1
        elif td['status'] == 'FAIL':
            tfal = tfal + 1

    if tname == "asset_homecontent":
        tname = 'ASSET API FOR HOMECONTENTS TEST RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "asset_allrisks":
        tname = 'ASSET API FOR ALL RISKS TEST RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "asset_vehicle":
        tname = 'ASSET API FOR MOTOR VEHICLES TEST RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "asset_personal_liability":
        tname = 'ASSET API FOR PERSONAL LIABILITY TEST RATING FATORS'
        rname = 'LIBERTY STI -  API GATEWAY '
    elif tname == "quote_to_policy":
        tname = 'ASSET API - END TO END FLOW - TEST PROCESS '
        rname = 'LIBERTY STI -  API GATEWAY '



    return render(request,'test_report.html',{
                                                'suitename':tname,
                                                'reporttitle':rname,
                                                'testcases':tcase,
                                                'timetaken':ttake,
                                                'starttime':tstrt,
                                                'endtime':tendt,
                                                'totaltests':texe,
                                                'totalpass':tpas,
                                                'totalfail':tfal
                                                })

def download_log(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/test_chamber")
    log_file = os.path.join(LOG_DIR,logfil)
    print(log_file)

    if os.path.exists(log_file):
        print('log file found!!')

        with open(log_file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/json")
            #response['Content-Disposition'] = 'attachment; filename="logfile.json"'
            response['Content-Disposition'] = 'attachment; filename='+logfil+''
            return response


def download_trace(request):
    # file = open('/path/to/yourfiles.zip', 'wb')
    # zf = zipfile.ZipFile(file, mode='w', compression=zipfile.ZIP_DEFLATED)
    # for fn in os.listdir("/tmp"):
    #     path = os.path.join("/tmp", fn)
    #     if os.path.isfile(path):
    #         try:
    #             zf.write(path)
    #         except IOError:
    #             pass
    # zf.close()
    tdir = trace_q

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/Log_data/")
    TRACE_DIR = os.path.join(BASE_DIR, "testapi/Log_data/"+tdir+"")
    print(TRACE_DIR)
    shutil.make_archive(TRACE_DIR,'zip',LOG_DIR,tdir)

    TRACE_DIR = os.path.join(BASE_DIR, "testapi/Log_data/"+tdir+".zip")



    try:
        assert os.path.exists(TRACE_DIR)
        print('Trace dir found!!')

        zip_file = open(TRACE_DIR, 'rb')
        response = HttpResponse(zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename='+tdir+'.zip'
        return response
    except:
        print("Directory not available")
        return render(request,'inspector_home.html')



def download_assetrr(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/test_chamber")

    log_file = os.path.join(LOG_DIR,asset_rrl)
    print(log_file)

    if os.path.exists(log_file):
        print('log file found!!')

        with open(log_file, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/json")
            #response['Content-Disposition'] = 'attachment; filename="logfile.json"'
            response['Content-Disposition'] = 'attachment; filename='+asset_rrl+''
            return response


@login_required
def beanstalk_home(request):
    return render(request, 'beanstalk_home.html')




@login_required
def beanstalk_asset(request):

    try:
        assert request.method == 'POST'

        motor_sel   = request.POST.getlist("motor[]")
        content_sel = request.POST.getlist("content[]")
        allrisk_sel = request.POST.getlist("allrisk[]")
        building_sel = request.POST.getlist("building[]")
        persliab_sel = request.POST.getlist("persliab[]")


        print(motor_sel)
        print(content_sel)
        print(allrisk_sel)
        print(building_sel)
        print(persliab_sel)

        try:

            assert (motor_sel != [] or content_sel != [] or allrisk_sel != [])

            aops = asset_manager()
            print('motor selection',motor_sel)
            motord = aops.get_vehicles('get_vehicle', motor_sel)

            asset_dict = {
                            'motor_list':motord,
                            'content_list':content_sel,
                            'allrisk_list':allrisk_sel,
                'building_list': building_sel,
                'persliab_list': persliab_sel
                         }

            asset_api_req = aops.asset_composer(asset_dict)
            print(asset_api_req)

            return render(request, 'beanstalk_asset_quoting.html',{'pantit':'crq','Req_data':asset_api_req})

        except:
            asset_error = {"asset_error" : "You cannot execute the API without adding any assets.."}
            return render(request,'beanstalk_asset_home.html',asset_error)


    except:

        getm = asset_manager()
        carslist = getm.process_carlist()
        print(carslist)
        return render(request, 'beanstalk_asset_home.html',{'carlist':carslist})


@login_required
def asset_execution(request):
    global asset_rrl,aquotn

    # ENTERING CREATE QUOTE

    try:
        assert request.method == 'POST' and request.POST.get('crpost')
        # testing...
        # time.sleep(5)
        # return render(request, 'beanstalk_asset_home.html')

        print("Hello....")

        alog = log_builder('asset_api')
        logger = alog.set_log('INFO', 'noformat')

        logger.info('CREATE QUOTE LOG ---------')
        logger.info('API Request(Asset API):--')

        asset_req = request.POST.get('content')
        logger.info(asset_req)
        gops = gateway_process('asset_api')
        print("hi..")
        asset_resp = gops.api_exec(asset_req)
        print("asset response..",asset_resp)
        logger.info('API Response(Asset API):--')

        print(asset_resp)

        asset_resp_dat = asset_resp[0]
        asset_respcode = asset_resp[1]

        # assert asset_resp_dat['quoteNumber']
        # aquotn = asset_resp_dat['quoteNumber']
        # print("quote number", aquotn)
        #
        # asset_resp_dat = json.dumps(asset_resp_dat, indent=5)
        #
        # print(asset_resp_dat)
        #
        # logger.info(asset_resp_dat)
        # asset_rrl = alog.return_file()
        #
        # # get Calculate prodata quote....
        # aops = asset_manager()
        # accept_q = aops.calculate_prorata(aquotn)
        # print(accept_q)
        # print('calculate prorata:', accept_q)
        #
        # return render(request, 'beanstalk_asset_quoting.html', {
        #     'pantit': 'acq',
        #     'Resp_data': asset_resp_dat,
        #     'dispq': aquotn,
        #     'Req_data': accept_q,
        #     'result': 'Success',
        #     'stat': asset_respcode,
        #     'run_trace': 'go'
        # })


        if asset_respcode == 200:
            try:
                assert asset_resp_dat['quoteNumber']
                aquotn = asset_resp_dat['quoteNumber']
                print("quote number",aquotn)

                asset_resp_dat = json.dumps(asset_resp_dat, indent=5)

                logger.info(asset_resp_dat)
                asset_rrl = alog.return_file()

                #get Calculate prodata quote....
                aops = asset_manager()
                accept_q = aops.calculate_prorata(aquotn)

                print('calculate prorata:',accept_q)

                return render(request, 'beanstalk_asset_quoting.html', {
                                                                         'pantit': 'acq',
                                                                         'Resp_data': asset_resp_dat,
                                                                         'dispq':aquotn,
                                                                         'Req_data':accept_q,
                                                                         'result':'Success',
                                                                         'stat': asset_respcode,
                                                                         'run_trace':'go'
                                                                       })
            except:
                print(type(asset_resp))
                if type(asset_resp) != str:
                    asset_resp = json.dumps(asset_resp, indent=5)

                logger.info(asset_resp)
                asset_rrl = alog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'crq',
                    'Resp_data':asset_resp,
                    'Req_data': 'Error in processing your quote. Please see the below response from API Gateway',
                    'stat': asset_respcode,
                    'result': 'Fail'

                })
        else:

            print(type(asset_resp))
            if type(asset_resp) != str:
                asset_resp = json.dumps(asset_resp, indent=5)

            logger.info(asset_resp)
            asset_rrl = alog.return_file()
            return render(request, 'beanstalk_asset_quoting.html', {
                'pantit': 'crq',
                'Resp_data': asset_resp,
                'Req_data': 'Error in processing your quote. Please see the below response from API Gateway',
                'stat': asset_respcode,
                'result': 'Fail'

            })
    except:
        pass

    # ENTERING ACCEPT QUOTE

    try:
        assert request.method == 'POST' and request.POST.get('acpost')

        accept_req = request.POST.get('content')

        gops = gateway_process('calculate_prorata')
        accept_resp = gops.api_exec(accept_req)

        clog = log_builder('asset_api_calcpror')
        logger = clog.set_log('INFO', 'noformat')
        logger.info('CALCULATE PRORATA LOG ---------')
        logger.info('API Request(Asset API):--')

        logger.info(accept_req)

        logger.info('API Response(Asset API):--')

        print(accept_resp)

        accept_resp_dat = accept_resp[0]
        accept_respcode = accept_resp[1]
        print(accept_resp_dat['referenceNumber'])

        if accept_resp:
            try:
                assert accept_resp_dat['referenceNumber']
                aquotr = accept_resp_dat['referenceNumber']

                accept_resp_dat = json.dumps(accept_resp_dat, indent=5)

                logger.info(accept_resp_dat)
                asset_rrl = clog.return_file()

                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit':'ctp',
                    'Resp_data': accept_resp_dat,
                    'dispq': aquotr,
                    'go_conv':'go',
                    'stat': accept_respcode,
                    'result': 'Success'
                })
            except:

                accept_resp_dat = json.dumps(accept_resp_dat, indent=5)

                logger.info(accept_resp_dat)
                asset_rrl = clog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'acq',
                    'Resp_data': accept_resp_dat,
                    'Req_data': 'Error while accept quoting. Please see the below response from API Gateway',
                    'stat': accept_respcode,
                    'result': 'Fail'
                })

    except:

        pass

    # ENTERING CONVERT QUOTE TO POLICY

    try:

        assert request.method == 'POST' and request.POST.get('ctpost')

        policy_n = request.POST.get('convtop')
        print(policy_n)

        gops = gateway_process("convert_to_policy")
        conv_resp = gops.convtop_exec(policy_n)

        dlog = log_builder('asset_api_conv_to_policy_')
        logger = dlog.set_log('INFO', 'noformat')
        logger.info('CONVERT TO POLICY LOG ---------')
        logger.info('API Request(Asset API):--')

        logger.info(policy_n)

        logger.info('API Response(Asset API):--')

        conv_resp_dat = conv_resp[0]
        conv_respcode = conv_resp[1]


        if conv_resp:
            try:

                assert conv_resp_dat['policyNumber']
                aquotr = conv_resp_dat['policyNumber']


                log_policy('Req quote data',aquotr, "tester")

                conv_resp_dat = json.dumps(conv_resp_dat, indent=5)

                logger.info(conv_resp_dat)
                asset_rrl = dlog.return_file()



                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'ctp',
                    'Resp_data': conv_resp_dat,
                    'dispq': aquotr,
                    'go_conv':'complete',
                    'stat': conv_respcode,
                    'result': 'Success'
                })
            except:

                conv_resp_dat = json.dumps(conv_resp_dat, indent=5)

                logger.info(conv_resp_dat)
                asset_rrl = dlog.return_file()
                return render(request, 'beanstalk_asset_quoting.html', {
                    'pantit': 'ctp',
                    'Resp_data': conv_resp_dat,
                    'go_conv': 'go',
                    'Req_data': 'Error while accept quoting. Please see the below response from API Gateway',
                    'stat': conv_respcode,
                    'result': 'Fail'
                })

    except:
        pass

    # ENTERING AMEND QUOTE:

    try:

        assert request.method == 'POST' and request.POST.get('amqpost')

        print("Inside Amend quote!!..")

        amquote = aquotn
        print(amquote)

        amdq = gateway_process('amend_quote')
        amdq_data = amdq.view_quote(amquote)

        amdq_data = amdq_data[0]

        amdq_data = json.dumps(amdq_data, indent=5)

        return render(request, 'beanstalk_asset_quoting.html', {'pantit': 'amdq', 'Req_data': amdq_data})

    except:

        return render(request, 'beanstalk_asset_quoting.html')



@login_required
def beanstalk_policy(request):
    try:
        request.method == 'POST'
        ampost = request.POST.get('ampost')
        amlpost = request.POST.get('amlpost')

        print(amlpost)
        print(ampost)


        if ampost == 'Proceed':
            policyn = request.POST.get('policyn')

        elif amlpost == 'Proceed':
            policyn = request.POST.get('psel')

        amdpol = gateway_process('view_policy')
        amdata = amdpol.view_policy(policyn)

        amdata = amdata[0]

        amdata = json.dumps(amdata,indent=5)
        #offline process - amend
        """
        amdata = offline_adder(selected_policy)
        return render(request, 'beanstalk_amendment.html',{
            "amd_data":amdata,
            "pantit": "amq"
        })"""
        #offline ends


        return render(request,'beanstalk_amendment.html',{
            "amd_data":amdata,
            'amdresp_data': '',
            "pantit": "amdp"
        })
    except:
        print("Generating the policy list..")
        startpol = Policy_starter("get_policy")
        policy_list = startpol.policy_base()
        print(policy_list)
        return render(request, 'beanstalk_exe2.html', {"polist": policy_list})





@login_required
def policy_endorsement(request):
    global amd_reqv1,policynum,asset_rrl,amd_reqv2

    try:
        assert request.method == 'POST' and request.POST.get('amdpost')
        print("Policy Endorsement process started...")
        amd_reqv1 = request.POST.get('content')

        print(amd_reqv1)
        print(type(amd_reqv1))
        alog = log_builder('policy_api')
        logger = alog.set_log('INFO', 'noformat')

        logger.info('POLICY ENDORSEMENT LOG ---------')
        logger.info('API Request(Amend Policy):--')
        logger.info(amd_reqv1)


        amd_reqv1d = json.loads(amd_reqv1)
        pol_head = amd_reqv1d['policyHeader']
        policynum = pol_head['policyNumber']
        #
        # view_pol = pol_head['policyNumber']
        # print(view_pol)

        proc_pol = gateway_process('process_policy')

        amdpol = proc_pol.process_policy(amd_reqv1)

        print("asset response..", amdpol)
        logger.info('API Response(Amend Policy ):--')

        print(amdpol)

        amdpol_dat = amdpol[0]
        amdpol_respcode = amdpol[1]


        if amdpol_respcode == 200:
            try:

                #print("quote number",aquotn)

                amdpol_dat = json.dumps(amdpol_dat, indent=5)

                logger.info(amdpol_dat)
                asset_rrl = alog.return_file()


                print(type(amdpol_dat))

                return render(request, 'beanstalk_amendment.html',{
                                                                         'pantit':'adpa',
                                                                         'amdresp_data': amdpol_dat,
                                                                         'dispq':'POLICY',
                                                                         'result':'Success',
                                                                         'stat': amdpol_respcode,
                                                                         'run_trace':'go'
                                                                    })
            except:

                return render(request, 'beanstalk_exe2.html')


        else:

            print(type(amdpol_dat))
            if type(amdpol_dat) != str:
                amdpol_dat = json.dumps(amdpol_dat, indent=5)

            logger.info(amdpol_dat)
            asset_rrl = alog.return_file()
            return render(request, 'beanstalk_amendment.html', {
                'pantit': 'amdp',
                'Resp_data': amdpol_dat,
                'Req_data': 'Error in processing your Policy amendment. Please see the below response from API Gateway',
                'stat': amdpol_respcode,
                'result': 'Fail'

            })


    except:
        pass

    try:
        assert request.method == 'POST' and request.POST.get('acdpost')

        print("Accept/Decline process started....")
        acdval = request.POST.get('adsel')
        print(acdval)

        if acdval == "Accept":
            acdval = "True"
        elif acdval == "Decline":
            acdval = "False"

        alog = log_builder('accept_policy')
        logger = alog.set_log('INFO', 'noformat')

        logger.info('POLICY ENDORSEMENT LOG ---------')
        logger.info('API Request(Accept/Decline Policy Endorsement):--')
        logger.info(acdval)


        policyn = policynum

        acdpol = gateway_process('accept_policy')
        acdresp = acdpol.accept_policyendorse(policynum,acdval)

        acdresp_dat = acdresp[0]
        acdrespcode = acdresp[1]



        if acdrespcode == 200:
            try:
                #print("quote number",aquotn)

                acdpol_dat = json.dumps(acdresp_dat, indent=5)

                amd_reqv2 = acdpol_dat

                logger.info(acdpol_dat)
                asset_rrl = alog.return_file()

                print(type(acdpol_dat))

                return render(request, 'beanstalk_amendment.html',{
                                                                         'pantit':'comp',
                                                                         'amdresp_data': acdpol_dat,
                                                                         'dispq':policynum,
                                                                         'result':'Success',
                                                                         'stat': acdrespcode,
                                                                         'run_trace':'go'
                                                                    })
            except:
                return render(request, 'beanstalk_exe2.html')


        else:

            print(type(acdresp_dat))
            if type(acdresp_dat) != str:
                acdpol_dat = json.dumps(acdresp_dat, indent=5)

            logger.info(amdpol_dat)
            asset_rrl = alog.return_file()
            return render(request, 'beanstalk_amendment.html', {
                'pantit': 'comp',
                'amdresp_data': acdpol_dat,
                'dispq': policynum,
                'result': 'Fail',
                'stat': acdrespcode,
                'run_trace': 'go'

            })

    except:
        pass




def policy_versioning(request):


    return render(request,'beanstalk_transition.html',{

        "bview_data":amd_reqv1,
        "aview_data":amd_reqv2

    })


def inspector_tag(request):

    global tdirn,trace_q

    try:
        assert request.method == 'POST'
        trace_q = request.POST.get("traceqn")
        print('tracing quote....',trace_q)

        # time.sleep(4)

        # return render(request,'inspector_home.html',{'trace_resp':'show'})

        quoteno = trace_q

        ratingsrv = Rating_engine()

        tdirn = ratingsrv.direct_log(quoteno)

        get_me = ['rengreq', 'xml']

        req_rmpath = '/Volumes/Liberty.PolicyAdmin Debugging/'
        xmlio_rmpath = '/Volumes/RatingEngine/CalculationOutput/'

        for gtm in get_me:
            if gtm == 'xml':
                prefile = quoteno
                rmpath = xmlio_rmpath
            elif gtm == 'rengreq':
                prefile = 'RatingEngineRequest_' + quoteno
                rmpath = req_rmpath

            ratingsrv.rating_trap(rmpath, prefile)

        return render(request,'inspector_home.html',{'trace_resp':'show'})


    except:
        pass

    return render(request,'inspector_home.html')

@login_required
def beanstalk_amendment(request):
    global view_before
    global view_after
    global amdp
    incom_post_amq = False
    incom_post_adp = False

    if request.method == 'POST':
        ampost = request.POST.get('amdpost')
        adpost = request.POST.get('aacpost')
        vtpost = request.POST.get('vtrpost')

        print(ampost)

        if ampost is not None:
            # offline ends
            incom_post = ampost
            amd_req = request.POST.get('content')
            amd_req = json.loads(amd_req)
            view_pol = amd_req['PolicyNumber']
            print("Posted...",incom_post)
        elif adpost is not None:
            incom_post = adpost
            incom_decsn = request.POST.get('adsel')
        elif vtpost is not None:
            incom_post = vtpost
        else:
            pass


        if incom_post == 'PROCEED WITH POLICY AMENDMENT':
            view_before = con_gatepro_get(view_pol, request, 'view_policy')
            presp_data = con_gatepro(amd_req, request, 'amend_quote')
            incom_post_amq = True
        elif incom_post == 'PROCEED WITH THIS DECISION':
            startmon = Policy_starter('acdec_amend')
            acd_reqdata = startmon.accept_amendment(amdp,incom_decsn)
            presp_data = con_gatepro(acd_reqdata, request, 'acdec_amend')
            incom_post_adp = True
        elif incom_post == 'VIEW CHANGES':
            view_before = con_gatepro_get(view_pol, request, 'view_policy')
            incom_post_vtr = True
            return render(request, 'beanstalk_transition.html', {
                'bview_data': view_before,
                'aview_data':view_after
            })
        else:
            pass


        prdata = json.loads(presp_data)
        print(prdata)
        print(type(prdata))
        #req_bankd = json.loads(amd_req)




        if prdata['bSuccess'] is True:
            if incom_post_amq is True:
                amdp = prdata['QuoteNumber']
                print("...............INSIDE AMEND PROCESS AND ACCEPT/DECLINE RETURN............................")
                return render(request, 'beanstalk_amendment.html', {
                    'pantit': 'aac',
                    'dispq': amdp,
                    'Resp_data': presp_data,
                    'stat': 'Success'
                })
            if incom_post_adp is True:
                return render(request, 'beanstalk_amendment.html', {
                    'pantit': 'comp',
                    'dispq': amdp,
                    'Resp_data': presp_data,
                    'stat': 'Success'
                })
        elif prdata['bSuccess'] is False:
            context_dict = {'text': 'API Gateway testing channel - TAG'}
            return render(request, 'tag_home.html', context_dict)
    else:
        context_dict = {'text': 'API Gateway testing channel - TAG'}
        return render(request, 'tag_home.html', context_dict)


def tag_user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                goahead = 'userin'
                return HttpResponseRedirect(reverse(index))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Login failed against the below user details")
            lresp = 'invalid login details supplied!. Please retry or contact your admin'
            return render(request,'tag_login.html',{"eresp":lresp})
    else:
        return render(request,'tag_login.html',{})




def tag_register(request):

    registered = False

    if request.method == "POST":
        user_form = Userform(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = Userform()

    return render(request,'tag_register.html', {'user_form':user_form,
                                                'registered':registered})




@login_required
def special(request):
    return  HttpResponse("You are logged in, Nice!")


@login_required
def tag_user_logout(request):
    logout(request)
    return render(request,'tag_login.html')


def log_policy(quotes,policy_n,tuser):
    logpol = Policy_api("log_policy")
    logpol.policy_log(tuser,policy_n,quotes)


def offline_pro(quotes,request):
    startoff = Composer('policy_hub')
    startoff.load_man(quotes)


def offline_adder(selectp):
    startadd = Composer('policy_hub')
    startadd.perform_tokens()
    amdata = startadd.amendpro(selectp)
    return amdata




