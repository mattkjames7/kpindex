from . import Globals
import PyFileIO as pf
import numpy as np
import datetime

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

def _ListFiles(currYear):

	"""
	
	Generate a list of specific file names for a given year range.
	
	The function creates a list of filenames in the format 'Kp_ap_YYYY.txt', where YYYY ranges from 1932 to the current year specified.
	
	Args:
	    currYear (int): The current year up to which the filenames will be generated.
	
	Returns:
	    list of str: A list containing filenames for each year from 1932 to currYear.
	
	"""
	#we need a list of specific file names
	#as this directory oin the FTP site now
	#stores multiple different types of files
	years = np.arange(1932,currYear+1)
	fnames = ['Kp_ap_{:04d}.txt'.format(y) for y in years]

	return fnames


def _ParseFTP():
	"""
	
	Parses the FTP index file to read file names and their associated update dates.
	
	This routine will read the FTP index file looking for specific file names
	related to 'omni_min' or 'omni_5min' and extract their update dates and FTP
	addresses.
	
	Returns:
	    tuple: A tuple containing three numpy arrays:
	        - FileNames (np.array): The list of file names extracted from the FTP index.
	        - Addresses (np.array): The corresponding FTP addresses for the files.
	        - UpdateDates (np.array): The update dates associated with the files in the format YYYYMMDD.
	
	
	"""
	

	#get the current year
	today = datetime.datetime.today()
	currYear = np.int32(today.strftime('%Y'))

	#list of files to look for
	files = _ListFiles(currYear)

	#read the file in
	fname = Globals.DataPath+'tmp/index.html'
	lines = pf.ReadASCIIFile(fname)
	nl = np.size(lines)
	
	#firstly, search for the lines which contain 'omni_min' or 'omni_5min'
	use = np.zeros(nl,dtype='bool')
	for i in range(0,nl):
		isgd = False
		for f in files:
			if f in lines[i]:
				isgd = True
		if isgd:
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
			yr = currYear
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
