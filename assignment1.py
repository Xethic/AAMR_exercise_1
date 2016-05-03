import sys

def maketable():
	table = dict()
	maturetable = dict()
	#for i in range (1, 22):	
	with open(str(sys.argv[1])) as mfile:
		mature = []
	#with open ("mature_"+str(i)+".fa") as mfile:
		for line in mfile:				
			
			if line[0] == ">":					
				name = line.split(" ")
								
				miname = name[0][1:-1]
				
				if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
					continue
				
					
				
										
				mature.append(' '.join(name[1:])[:-1])
				print mature
				#mature.append(name[1])
				#maturetable[miname] = mature 
			else:
					
				if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
					continue
									
				#mature = maturetable[miname]
				mature.append(line[:-1])
				maturetable[miname.lower()] = mature
				mature = []
				
				
				
	#print maturetable	
				
				
	#with open("hairpin_"+str(i)+".fa") as hfile:
	with open(str(sys.argv[2])) as hfile:
		pre = []
		for line in hfile:
							
			if line[0] == ">":
									
				name = line.split(" ")
				
				miname = name[0][1:]
				
				if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
					continue
				
									
				if miname in table: 
					continue
					
				else:
					pre.append(' '.join(name[1:])[:-1])
				
				
				#mature.append(name[1])
					#table[miname] = pre 
			else:
				#preseq = table[miname]
				if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
					continue
					
				if miname in table: 
					continue
				
				if len(pre) == 2:
					pre[1] += line[:-1]
					if miname in maturetable:
						pre += maturetable[miname]
					table[miname] = pre
					pre = []
				else:
					pre.append(line[:-1])
					
				
				
	print table			


maketable()
