import sys

def convertmiRBaseV1ToLatest(filename):
	if(not isValidFileFormat(filename)):
		print'Could not read file! Aborting...'
		return 1
		
	infile = open(filename, 'r')
	nextLineSequence = False
	datasets = []
	identifier=''
	accessor = ''
	description = ''
	sequence = ''
	
	print 'Reading input file...'
	for line in infile:
		
		if(line.find('ID', 0, 2) != -1):
			words = line.split(' ')
			if(len(words) >= 4):
				identifier = words[3]
			continue
		
		if(line.find('AC', 0, 2) != -1):
			words = line.split(' ')
			if(len(words) >= 4):
				accessor = words[3]
			continue
		
		if(line.find('DE', 0, 2) != -1):
			words = line.split(' ')
			if(len(words) >= 4):
				description = words[3:]
			continue
		
		if(line.find('SQ', 0, 2) != -1):
			nextLineSequence = True;
			continue
			
		if(line.find('//', 0, 2) != -1):
			datapoint = (identifier, description, sequence) # accessor id is not required, but keep them for future purpose
			datasets.append(datapoint)
			sequence = ''
			nextLineSequence = False;
			continue
			
		if(nextLineSequence):
			words = line.split(' ')
			index = 5;
			while(index <= 10):
				index += 1
				if(len(words) > index):
					sequence += words[index]
				else:
					print 'Could not read Sequence data! Maybe wrong formatting? Aborting...'
					return 1
	
	infile.close()
	
	print 'Writing output to file...'
	
	filename = filename.rpartition('/')[2]
	filename = filename.rpartition('.')[0]
	filename = filename + '_converted.fa'
	outfile = open(filename,'w')
	for datapoint in datasets:
		if(len(datapoint) >= 3):
			outfile.write('>')
			outfile.write(str(datapoint[0]))
			for d in datapoint[1]:
				outfile.write(' ')
				outfile.write(str(d))
			outfile.write(str(datapoint[2]))
			outfile.write('\n')
		else:
			print 'Could not write output to file, sth. went wrong with the tuples! Aborting...'
			return 1
	outfile.close()
			
	print 'Finished!'
	return 0 

def isValidFileFormat(filename):
	extension = filename.rpartition('.')
	if(extension[2] != 'dat'):
		print'No .dat file found.'
		return False
	
	infile = open(filename, 'r')
	IDfound = False
	ACfound = False
	DEfound = False
	SQfound = False
	for line in infile:
		IDfound = True if IDfound else line.find('ID', 0, 1)
		ACfound = True if ACfound else line.find('AC', 0, 1)
		DEfound = True if DEfound else line.find('DE', 0, 1)
		SQfound = True if SQfound else line.find('SQ', 0, 1)
		if(IDfound and ACfound and DEfound and SQfound):
			return True
	return False

#####
# This small program converts miRBase version 1.0 .dat files into the latest .fa format.
#
#
#####	
convertmiRBaseV1ToLatest(str(sys.argv[1]))
