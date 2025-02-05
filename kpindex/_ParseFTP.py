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
	
	Generates a list of specific file names based on the current year.
	
	The function constructs file names for a series of years starting from 1932
	up to the specified current year. The file names are formatted as
	'Kp_ap_YYYY.txt', where YYYY is the year.
	
	Args:
	    currYear (int): The current year, which determines the range of years
	for which file names will be generated.
	
	Returns:
	    list: A list of strings representing the formatted file names for each
	year from 1932 to currYear.
	
	"""
	#we need a list of specific file names
	#as this directory oin the FTP site now
	#stores multiple different types of files
	years = np.arange(1932,currYear+1)
	fnames = ['Kp_ap_{:04d}.txt'.format(y) for y in years]

	return fnames


def _ParseFTP():
	"""
	
	Parses the FTP index file to extract file names and their associated update
	dates.
	
	This function reads the FTP index file to find specific file names
	containing 'omni_min' or 'omni_5min' along with their respective update
	dates. It filters the lines that match the criteria and processes them to
	extract the necessary information.
	
	Returns:
	    tuple: A tuple containing three numpy arrays:
	        - FileNames (numpy.ndarray): An array of file names found in the FTP
	index.
	        - Addresses (numpy.ndarray): An array of corresponding FTP addresses
	for the files.
	        - UpdateDates (numpy.ndarray): An array of update dates for the
	files in 'YYYYMMDD' format.
	
	
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
