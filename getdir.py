#----------------------------------------------------------------------------
import json, re, csv, unicodedata, string, sys, glob
from pathlib import Path
import pandas as pd
from subprocess import check_output

#---------------------------------------------------------------
initialdirectoryconfig = 'initialization.py'
#---------------------------------------------------------------
getdirectory = check_output([sys.executable, initialdirectoryconfig], universal_newlines=True)

print(getdirectory)