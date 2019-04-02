from . import Globals
import PyFileIO as pf
import numpy as np

def _KpStringtoFloat(kps):
	'''
	Converts Kp value string to a floating point e.g. '3+' -> 3.333.
	'''
	out = np.float32(kps[:-1])
	pm = kps[-1]
	if pm == '+':
		out += 1.0/3.0
	elif pm == '-':
		out -= 1.0/3.0
	return out
	

def _ReadKPTab(fname):
	'''
	Reads and tries to make some sense of the Kp index tab files.
	
	Input:
		fname: full file name and path to .tab file.
	
	Returns:
		numpy.recarray
	'''

	#define the data type
	dtype = Globals.dtype
	
	#read the file in
	lines = pf.ReadASCIIFile(fname)
	
	#remove lines which don't have any data
	n = 0
	while not ' ' in lines[n][0:6]:
		n+=1
	lines = lines[:n]
	
	#now we can start deciphering the file
	w0 = [0,8,11,14,17,21,24,27,30,35,39,43,46]
	w1 = [6,10,13,16,19,23,26,29,32,38,42,45,49]
	out = np.recarray(n*8,dtype=dtype)
	p = 0
	for i in range(0,n):
		#line by line
		l = lines[i]
		
		
		#date
		datestr = l[w0[0]:w1[0]]
		if datestr[0] == '9':
			add = 19000000
		else:
			add = 20000000
		Date = np.int32(datestr) + add
		
		
		#Sum
		Sum = _KpStringtoFloat(l[w0[9]:w1[9]])
		
		#Activity
		Act = l[w0[10]:w1[10]]
		
		#Ap
		Ap = np.int32(l[w0[11]:w1[11]])
		
		#Cp
		Cp = np.float32(l[w0[12]:w1[12]])
		
		#3-hourly
		for j in range(0,8):
			out.ut0[p] = j*3.0
			out.ut1[p] = (j+1)*3.0
			out.Date[p] = Date
			out.Sum[p] = Sum
			out.Activity[p] = Act 
			out.Ap[p] = Ap
			out.Cp[p] = Cp
			out.Kp[p] = _KpStringtoFloat(l[w0[1+j]:w1[1+j]])
			p += 1
		
	return out
