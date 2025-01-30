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
	This function returns a list of file names corresponding to the given year range.
	
	Args:
	    currYear (int): The current year for which to generate file names. This is used to create an inclusive range from 1932 up to this year.
	
	Returns:
	    list: A list containing the file names in the format 'Kp_ap_{:04d}.txt', where {:04d} represents a zero-padded four-digit number for the year.
	"""
	#we need a list of specific file names
	#as this directory oin the FTP site now
	#stores multiple different types of files
	years = np.arange(1932,currYear+1)
	fnames = ['Kp_ap_{:04d}.txt'.format(y) for y in years]

	return fnames


def _ParseFTP():
	"""
	This function parses FTP index files to extract file names and their associated update dates. The function reads the specified index.html file from the DataPath temporary directory, processes it, and returns lists of file names, FTP addresses, and update dates.
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
