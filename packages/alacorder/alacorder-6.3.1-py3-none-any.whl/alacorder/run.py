# alacorder beta 0.6.3

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
import PyPDF2 as pdfs
from alacorder import alac
import warnings

# -> dict {mode, batch_size, case_max, tot_batches, batches: List[List[paths: str]]} 
# -> start() takes one argument - Config() - sets global values, gets to work 
# -> Config:

def config(in_path: str, out_path: str, special_config="", print_log=True, warn=False): 

	# Get extensions
	out_ext: str = out_path.split(".")[-1].strip()
	in_ext: str = in_path.split(".")[-1].strip() if len(in_path.split(".")[-1])<5 else "directory" 

	# Check if input path is valid
	if in_ext != "directory" and in_ext != "pkl" and in_ext != "csv" and in_ext != "xls" and in_ext != "json":
		raise Exception("Input path must be to/pdf/directory/, (archive).csv, (archive).xls, (archive).json, or (archive).pkl!")
	if os.path.exists(in_path) == False:
		raise Exception("Input path does not exist!")

	# Check if output path is valid
	if out_ext != "pkl" and out_ext != "txt" and out_ext != "csv" and out_ext != "xls" and out_ext != "json" and out_ext != "dta":
		raise Exception("Output path must be .csv, .xls, .json, or .pkl! (.pkl only for full text archives)")

	# Set read, write modes, contents
	if in_ext == "directory" and out_ext == "pkl": # from dir to pkl = make archive
		make = "archive"
		origin = "directory"
		contents = glob.glob(in_path + '**/*.pdf', recursive=True)
	elif in_ext == "directory" and bool(out_ext == "xls" or out_ext == "json" or out_ext == "csv" or out_ext == "txt" or out_ext == "dta"):
		make = "table"
		origin = "directory"
		contents = glob.glob(in_path + '**/*.pdf', recursive=True)
	elif in_ext == "pkl":
		make = "table"
		origin = "archive"
		contents = pd.read_pickle(in_path)['Path']
	elif in_ext == "csv":
		make = "table"
		origin = "archive"
		contents = pd.read_csv(in_path).tolist()
	elif in_ext == "xls":
		make = "table"
		origin = "archive"
		contents = pd.read_excel(in_path,sheet_name="text_from_pdf")
	elif in_ext == "json": 
		make = "table"
		origin = "archive"
		contents = pd.read_pickle(in_path)
	else:
		raise Exception("Not supported. Refer to alacorder documentation on github for supported input and output modes.")

	# verify directory input has content
	if len(contents)==0:
		raise Exception("No cases found in input path! (" + in_path + ")")

	if origin == "archive":
		batchsize = 100
	if origin == "directory":
		batchsize = 50

	case_max = len(contents)
	tot_batches = math.ceil(case_max / batchsize)

	batches = np.array_split(contents, tot_batches)

	if print_log == True:
		print(f"Initial configuration succeeded!\n\n{in_path} ----> {out_path}\n\n{case_max} cases in {tot_batches} batches")

	config = pd.Series({
		'in_path': in_path,
		'out_path': out_path,
		'in_ext': in_ext,
		'out_ext': out_ext,
		'origin': origin,
		'make': make,
		'contents': contents,
		'batches': batches,
		'case_max': case_max,
		'tot_batches': tot_batches,
		'batchsize': batchsize,
		'print_log': print_log,
		'warnings': warn
	})
	
	return config

def log_complete(config, start_time):
	path_in = config['in_path']
	path_out = config['out_path']
	case_max = config['case_max']
	bsize = config['batchsize']
	completion_time = time.time()
	elapsed = completion_time - start_time
	cases_per_sec = case_max/elapsed
	print(f'''
    ___    __                          __         
   /   |  / /___ __________  _________/ /__  _____
  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																										
	
	ALACORDER beta 6.3
	by Sam Robson	

	Searching {path_in} 
	Writing to {path_out} 

	TASK SUCCEEDED ({case_max}/{case_max} cases)
	Completed export in {elapsed:.2f} seconds ({cases_per_sec:.2f}/sec)

''') 

def console_log(config, on_batch: int, to_str: str):
	path_in = config['in_path']
	path_out = config['out_path']
	case_max = config['case_max']
	bsize = config['batchsize']
	plog = config['print_log']
	if plog == True:
		print(to_str)
		print(f'''
	    ___    __                          __         
	   /   |  / /___ __________  _________/ /__  _____
	  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
	 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
	/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																											
		
		ALACORDER beta 6.3
		by Sam Robson	

		Searching {path_in} 
		Writing to {path_out} 

		Exported {on_batch*bsize} of {case_max}

	''') 

	if plog == False:
		print(f'''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
		    ___    __                          __         
		   /   |  / /___ __________  _________/ /__  _____
		  / /| | / / __ `/ ___/ __ \\/ ___/ __  / _ \\/ ___/
		 / ___ |/ / /_/ / /__/ /_/ / /  / /_/ /  __/ /    
		/_/  |_/_/\\__,_/\\___/\\____/_/   \\__,_/\\___/_/     
																																												
			
			ALACORDER beta 6.3
			by Sam Robson	

			Searching {path_in} 
			Writing to {path_out} 

			Exported {on_batch*bsize} of {case_max}

		''') 

def writeArchive(config):

	path_in = config['in_path']
	path_out = config['out_path']
	case_max = config['case_max']
	tot_batches = config['tot_batches']
	batchsize = config['batchsize']
	batches = config['batches']
	contents = config['contents']
	in_ext = config['in_ext']
	out_ext = config['out_ext']
	print_log = config['print_log']
	warn = config['warnings']

	if warn == False:
		warnings.filterwarnings("ignore")

	start_time = time.time()
	outputs = pd.DataFrame()
	on_batch = 0

	for b in batches:

		paths = pd.Series(b)
		allpagestext = pd.Series(b).map(lambda x: alac.getPDFText(x))
		timestamp = time.time()

		c = pd.DataFrame({
			'Path': paths,
			'AllPagesText': allpagestext,
			'Timestamp': timestamp
			})
		outputs = pd.concat([outputs, c],ignore_index=True)
		on_batch += 1
		outputs.fillna('',inplace=True)

		if out_ext == "pkl":
			outputs.to_pickle(path_out)
		elif out_ext == "json":
			outputs.to_json(path_out)
		elif out_ext == "csv":
			outputs.to_csv(path_out,escapechar='\\')
		elif out_ext == "md":
			outputs.to_markdown(path_out)
		elif out_ext == "txt":
			outputs.to_string(path_out)
		elif out_ext == "dta":
			outputs.to_stata(path_out)
		console_log(config, on_batch, "")
	log_complete(config, start_time)
	on_batch = 0

def writeTables(config):
	batches = config['batches']
	path_in = config['in_path']
	path_out = config['out_path']
	case_max = config['case_max']
	tot_batches = config['tot_batches']
	batchsize = config['batchsize']
	in_ext = config['in_ext']
	out_ext = config['out_ext']
	print_log = config['print_log']
	warn = config['warnings']
	contents = config['contents']
	batches = config['batches']
	if warn == False:
		warnings.filterwarnings("ignore")
	start_time = time.time()
	on_batch = 0
	outputs = pd.DataFrame()

	fees = pd.DataFrame({'CaseNumber': '', 'Code': '', 'Payor': '', 'AmtDue': '', 'AmtPaid': '', 'Balance': '', 'AmtHold': ''},index=[0])
	charges = pd.DataFrame({'CaseNumber': '', 'Num': '', 'Code': '', 'Felony': '', 'Conviction': '', 'CERV': '', 'Pardon': '', 'Permanent': '', 'Disposition': '', 'CourtActionDate': '', 'CourtAction': '', 'Cite': '', 'TypeDescription': '', 'Category': '', 'Description': ''},index=[0]) # charges = pd.DataFrame() # why is this here
	print(batches)
	for i, c in enumerate(batches):
		b = pd.DataFrame()
		b['AllPagesText'] = pd.Series(c).map(lambda x: alac.getPDFText(x))
		b['CaseInfoOutputs'] = b['AllPagesText'].map(lambda x: alac.getCaseInfo(x))
		b['CaseNumber'] = b['CaseInfoOutputs'].map(lambda x: x[0])
		b['Name'] = b['CaseInfoOutputs'].map(lambda x: x[1])
		b['Alias'] = b['CaseInfoOutputs'].map(lambda x: x[2])
		b['DOB'] = b['CaseInfoOutputs'].map(lambda x: x[3])
		b['Race'] = b['CaseInfoOutputs'].map(lambda x: x[4])
		b['Sex'] = b['CaseInfoOutputs'].map(lambda x: x[5])
		b['Address'] = b['CaseInfoOutputs'].map(lambda x: x[6])
		b['Phone'] = b['CaseInfoOutputs'].map(lambda x: x[7])
		b['ChargesOutputs'] = b.index.map(lambda x: alac.getCharges(b.loc[x].AllPagesText, b.loc[x].CaseNumber))
		b['Convictions'] = b['ChargesOutputs'].map(lambda x: x[0])
		b['DispositionCharges'] = b['ChargesOutputs'].map(lambda x: x[1])
		b['FilingCharges'] = b['ChargesOutputs'].map(lambda x: x[2])
		b['CERVConvictions'] = b['ChargesOutputs'].map(lambda x: x[3])
		b['PardonConvictions'] = b['ChargesOutputs'].map(lambda x: x[4])
		b['PermanentConvictions'] = b['ChargesOutputs'].map(lambda x: x[5])
		b['ConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[6])
		b['ChargeCount'] = b['ChargesOutputs'].map(lambda x: x[7])
		b['CERVChargeCount'] = b['ChargesOutputs'].map(lambda x: x[8])
		b['PardonChargeCount'] = b['ChargesOutputs'].map(lambda x: x[9])
		b['PermanentChargeCount'] = b['ChargesOutputs'].map(lambda x: x[10])
		b['CERVConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[11])
		b['PardonConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[12])
		b['PermanentConvictionCount'] = b['ChargesOutputs'].map(lambda x: x[13])
		b['ChargeCodes'] = b['ChargesOutputs'].map(lambda x: x[14])
		b['ConvictionCodes'] = b['ChargesOutputs'].map(lambda x: x[15])
		b['FeeOutputs'] = b.index.map(lambda x: alac.getFeeSheet(b.loc[x].AllPagesText, b.loc[x].CaseNumber))
		b['TotalAmtDue'] = b['FeeOutputs'].map(lambda x: x[0])
		b['TotalBalance'] = b['FeeOutputs'].map(lambda x: x[1])
		b['TotalD999'] = b['FeeOutputs'].map(lambda x: x[2])
		b['FeeCodesOwed'] = b['FeeOutputs'].map(lambda x: x[3])
		b['FeeCodes'] = b['FeeOutputs'].map(lambda x: x[4])
		b['FeeSheet'] = b['FeeOutputs'].map(lambda x: x[5])


		feesheets = b['FeeOutputs'].map(lambda x: x[6]) # -> pd.Series(df, df, df)
		feesheets = feesheets.dropna() # drop empty 
		feesheets = feesheets.tolist() # convert to list -> [df, df, df]
		feesheets = pd.concat(feesheets,axis=0,ignore_index=True) # add all dfs in batch -> df
		fees = pd.concat([fees, feesheets],axis=0,ignore_index=True)
		fees['AmtDue'] = fees['AmtDue'].map(lambda x: pd.to_numeric(x,'ignore'))
		fees['AmtPaid'] = fees['AmtPaid'].map(lambda x: pd.to_numeric(x,'ignore'))
		fees['Balance'] = fees['Balance'].map(lambda x: pd.to_numeric(x,'ignore'))
		fees['AmtHold'] = fees['AmtHold'].map(lambda x: pd.to_numeric(x,'ignore'))


		chargetabs = b['ChargesOutputs'].map(lambda x: x[17])
		chargetabs = chargetabs.dropna()
		chargetabs = chargetabs.tolist()
		chargetabs = pd.concat(chargetabs,axis=0,ignore_index=True)
		charges = pd.concat([charges, chargetabs],axis=0,ignore_index=True)
		print(chargetabs)

		b['ChargesTable'] = b['ChargesOutputs'].map(lambda x: x[-1])
		b['TotalD999'] = b['TotalD999'].map(lambda x: pd.to_numeric(x,'ignore'))
		b['TotalAmtDue'] = b['TotalAmtDue'].map(lambda x: pd.to_numeric(x,'ignore'))
		b['TotalBalance'] = b['TotalBalance'].map(lambda x: pd.to_numeric(x,'ignore'))
		b.drop(columns=['AllPagesText','CaseInfoOutputs','ChargesOutputs','FeeOutputs','TotalD999','ChargesTable','FeeSheet'],inplace=True)
		outputs = pd.concat([outputs, b],ignore_index=True)
		
		outputs.fillna('',inplace=True)
		charges.fillna('',inplace=True)
		fees.fillna('',inplace=True)

		# write 
		if out_ext == "xls":
			with pd.ExcelWriter(path_out) as writer:
				outputs.to_excel(writer, sheet_name="cases-table")
				fees.to_excel(writer, sheet_name="fees-table")
				charges.to_excel(writer, sheet_name="charges-table")
		elif out_ext == "pkl":
			outputs.to_pickle(path_out)
		elif out_ext == "json":
			outputs.to_json(path_out)
		elif out_ext == "csv":
			outputs.to_csv(path_out,escapechar='\\')
		elif out_ext == "md":
			outputs.to_markdown(path_out)
		elif out_ext == "txt":
			outputs.to_string(path_out)
		elif out_ext == "dta":
			outputs.to_stata(path_out)
		else:
			raise Exception("Output file extension not supported! Please output to .xls, .pkl, .json, or .csv")
		on_batch += 1
		console_log(config, on_batch, outputs[['CaseNumber','Name','DispositionCharges']])
	log_complete(config, start_time)
	on_batch = 0
