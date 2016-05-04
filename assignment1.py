import sys
import matplotlib.pyplot as plt
import pylab as pl

def maketable():
	table = dict()
	maturetable = dict()
	for i in range (2, 22):	
		#with open(str(sys.argv[1])) as mfile:
		with open ("mature_"+str(i)+".fa") as mfile:
			mature = []
			for line in mfile:				
				
				if line[0] == ">":					
					name = line.split(" ")
									
					miname = name[0][1:-1]
					
					if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
						continue
					
						
					
											
					mature.append(' '.join(name[1:])[:-1])
					print mature
					#mature.append(name[1])
					maturetable[miname.lower()] = mature 
				else:
						
					if (miname[0:3] != "cel") and (miname[0:3] != "hsa") and (miname[0:3] != "mmu"):
						continue
										
					mature = maturetable[miname.lower()]
					mature.append(line[:-1])
					maturetable[miname.lower()] = mature
					mature = []
					
					
				
	#print maturetable	
				
				
		with open("hairpin_"+str(i)+".fa") as hfile:
		#with open(str(sys.argv[2])) as hfile:
			pre = []
			for line in hfile:
								
				if line[0] == ">":
					
					seq = ''.join(pre[1:])
					pre2 = 
					
										
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
					
					pre.append(line[:-1])
					
					if miname in maturetable:
						pre += maturetable[miname]
						pre.append(i)
					table[miname] = pre
					
					else:
						pre.append(line[:-1])
						
					
					
	print table	
	print len(table)		


maketable()






def precursorplot():
	
	versionlist = []
	prenumberscel = []
	prenumbershsa = []
	prenumbersmmu = []
	for k in range (2,22):
		versionlist.append(k)
	for i in range (2,22):
		with open("hairpin_"+str(i)+".fa") as f:
			countercel, counterhsa, countermmu = 0, 0, 0
			for line in f:
				if line[0] == ">":
					if line[1:4] == "cel":						
						countercel += 1
					else:
						if line[1:4] == "mmu":						
							countermmu += 1
						else:
							if line[1:4] == "hsa":						
								counterhsa += 1
							else:
								continue
			
			
			prenumberscel.append(countercel)
			prenumbershsa.append(counterhsa)
			prenumbersmmu.append(countermmu)


	plt.bar(versionlist, prenumberscel, color = "r")	
	#fig.savefig("precursor_cel.png")
	plt.title("precursor from cel")
	plt.show()

	plt.bar(versionlist, prenumbershsa, color = "y")	
	#fig.savefig("precursor_hsa.png")
	plt.title("precursor from hsa")
	plt.show()
	
	plt.bar(versionlist, prenumbersmmu, color = "b")	
	#fig.savefig("precursor_mmu.png")
	plt.title("precursor from mmu")
	plt.show()


def matureplot():
	
	versionlist = []
	matnumbers = []
	for k in range (2,22):
		versionlist.append(k)
	for i in range (2,22):
		with open("mature_"+str(i)+".fa") as f:
			counter = 0
			for line in f:
				if line[0] == ">":
					counter += 1
			
			
			matnumbers.append(counter)


	#pl.plot(versionlist, matnumbers)
	pl.bar(versionlist, matnumbers)
	#fig.savefig("matureplot.png")
	plt.title("mature miRNA per version")
	pl.show()
	
	
	
#precursorplot()
#matureplot()



def ratio():
	#ration precursor and mature mirna per species
	groups = [[2,8],[8,17],[17,20],[20,22]]
	mcel, mhsa, mmmu = 0, 0, 0
	hcel, hhsa, hmmu = 0, 0, 0
	
	ratiocel, ratiommu, ratiohsa = [],[],[]
	
	for g in groups:
		
		for i in range(g[0], g[1]):
			with open("mature_"+str(i)+".fa") as f:
				
				for line in f:
					if line[0] == ">":
						if line[1:4] == "cel":						
							mcel += 1
						else:
							if line[1:4] == "mmu":						
								mmmu += 1
							else:
								if line[1:4] == "hsa":						
									mhsa += 1
								else:
									continue
							
							
			with open("hairpin_"+str(i)+".fa") as f:
				
				for line in f:
					if line[0] == ">":
						if line[1:4] == "cel":						
							hcel += 1
						else:
							if line[1:4] == "mmu":						
								hmmu += 1
							else:
								if line[1:4] == "hsa":						
									hhsa += 1
								else:
									continue
							
		
		y1 = float(mcel) / float(hcel)
		y2 = float(mmmu) / float(hmmu)
		y3 = float(mhsa) / float(hhsa)
		
		ratiocel.append(y1)
		ratiommu.append(y2)
		ratiohsa.append(y3)
	
	
	
	
	xaxis = [1,2,3,4]

	plt.bar(xaxis, ratiocel)
	plt.show()
	
	plt.bar(xaxis, ratiommu)
	plt.show()
	
	plt.bar(xaxis, ratiohsa)
	plt.show()
	


#ratio()
		
				
		
def computecontent(string):
	ca, cc, cg, cu = 0,0,0,0
	
	for i in string:
		if i == "a":
			ca += 1
		else:
			if i == "c":
				cc += 1
			else:
				if i == "g":
					cg += 1
				else: 
					if i == "u":
						cu += 1
					
	contentsum = ca + cu + cg + cc
	
	a = float(ca) / float(contentsum)
	c = float(cc) / float(contentsum)
	g = float(cg) / float(contentsum)
	u = float(cu) / float(contentsum)
	
	print a, c, g, u  
						


computecontent("acgu")











