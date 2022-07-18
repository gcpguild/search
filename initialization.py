import re, os
from operator import itemgetter
from pathlib import Path
#------------------------------------------------------------------
basepath = "C:\\google\\cloud\\solution\\serpapi\\projects"
#-----------------------------------------------------------------
def mkingdirs(givenlist):
    mymanog = ''.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
workingdir = mkingdirs(basepath)
os.chdir(workingdir)
#-------------------------------------------------------------------
N = "\\"
cwd = os.getcwd()
myd = cwd.split(N)
#-----------------------------------------------------------------
def getstringswitch(check_string_name):
  
    dict={
           's0' : myd[0], 
           's1' : myd[1], 
           's2' : myd[2], 
           's3' : myd[3],
           's4' : myd[4],
           's5' : myd[5],
           'd'  : 'data',
           'max_gs' : 10
          }
    return dict.get(check_string_name, cwd)

givenlist = [basepath,N,getstringswitch(check_string_name = 'd')]

mkdirlist = mkingdirs(givenlist)

print (mkdirlist)