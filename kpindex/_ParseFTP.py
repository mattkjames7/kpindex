from . import Globals
import PyFileIO as pf
import numpy as np

months = { 	'Jan':1,
			'Feb':2,
			'Mar':3,
			'Apr':4,
			'May':5,
			'Jun':6,
			'Jul':7,
			'Aug':8,
			'Sep':9,
			'Oct':10,
			'Nov':11,
			'Dec':12 }
			
def _ParseFTP():
	'''
	This routine will read the FTP index file looking for file names
	and their associated update dates.
	
	'''
	#read the file in
	fname = Globals.DataPath+'tmp/index.html'
	lines = pf.ReadASCIIFile(fname)
	nl = np.size(lines)
	
	#firstly, search for the lines which contain 'omni_min' or 'omni_5min'
	use = np.zeros(nl,dtype='bool')
	for i in range(0,nl):
		if '.tab' in lines[i]:
			use[i] = True
	keep = np.where(use)[0]
	lines = lines[keep]
	nl = lines.size
	
	#now to extract the FTP address, file name and update dates
	UpdateDates = np.zeros(nl,dtype='object')
	Addresses = np.zeros(nl,dtype='object')
	FileNames = np.zeros(nl,dtype='object')
	
	# note: negative indices are important because additional data in some lines
	for i in range(0,nl):
		#deal with date first
		s = lines[i].split()	
		if ':' in s[-2]:
			yr = 2022
		else:
			yr = np.int32(s[-2])
		mn = months[s[-4]]
		dy = np.int32(s[-3])
		UpdateDates[i] = '{:08}'.format(yr*10000 + mn*100 + dy)
		
		#now let's get the ftp address
		Addresses[i] = Globals.ftpadress + s[-1]
		
		#now the file name
		FileNames[i] = s[-1]
		
	return FileNames,Addresses,UpdateDates
