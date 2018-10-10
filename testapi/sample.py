import os


from paramiko import SSHClient



#file = open("/Volumes/Liberty.PolicyAdmin Debugging/")



def rating_trap(rpath,rfile):
  rmpath = rpath

  list_of_files = os.listdir(rmpath)
  # print(list_of_files)
  each_file = list_of_files

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


def direct_log(quote_n):
  global dirn
  try:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    LOG_DIR = os.path.join(BASE_DIR, "testapi/Log_data/")
    dirn = LOG_DIR + quote_n
    os.mkdir(dirn)

  except FileExistsError:
    print("Directory already exist!!!")
    pass


  # os.mkdir('', 0755);....................check : run trace log

    # cpfile = os.path.join(dirpath, each_file)
    # os.popen('cp ' + cpfile + 'Rating_engine_req.log')

"""lines = file.readlines()
for line in lines:
    print(line)

file.close()
"""


if __name__ == '__main__':
  quoteno = 'SHL000012569'

  direct_log(quoteno)

  get_me = ['rengreq','xml']

  req_rmpath = '/Volumes/Liberty.PolicyAdmin Debugging/'
  xmlio_rmpath = '/Volumes/RatingEngine/CalculationOutput/'

  for gtm in get_me:
    if gtm == 'xml':
      prefile = quoteno
      rmpath = xmlio_rmpath
    elif gtm == 'rengreq':
      prefile = 'RatingEngineRequest_'+quoteno
      rmpath = req_rmpath

    rating_trap(rmpath,prefile)


