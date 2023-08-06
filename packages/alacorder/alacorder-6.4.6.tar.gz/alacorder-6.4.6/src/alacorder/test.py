# test.py - new cites test
# alacorder beta 6.4

# - add parentheses and decimals to cite DONE 
# - clean up descriptions DONE
# - change phone number to int DONE
# - change num to int
# - make archive and tables at same time mode 

import cython
import pyximport; pyximport.install()
import os
import sys
from io import StringIO
import glob
import re
import xlrd
import openpyxl
import math
import datetime
import time
import pandas as pd
import numpy as np
import PyPDF2 as pypdf
import run
import alac


desc_test = run.config("/Users/samuelrobson/Desktop/sampletwo/", "/Users/samuelrobson/Desktop/sampleoutcombo.xls")

run.tempArchive(desc_test)
