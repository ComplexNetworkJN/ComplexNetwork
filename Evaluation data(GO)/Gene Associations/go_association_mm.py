import sys

class GoAssociation:
	def __init__(self, id_filename, gene_to_ens_filename, go_filename, out_filename):
		outfile = open(out_filename, "w")
		idtoname = open(id_filename)
		genetoens = open(gene_to_ens_filename)
		gofile = open(go_filename)

		gene_ens = {}
		for line in genetoens:
			cols = line.split()
			if len(cols) == 2:
				gene_ens[cols[1]] = cols[0]
			elif len(cols) == 1:
				gene_ens[cols[0]] = None
		
		M1 = {}
		for line in idtoname:
			cols = line.split()
			M1[cols[0]] = []
			for name in cols:
				M1[cols[0]].append(name)
				if (name[0:4] == "ENSM"):
					if (gene_ens[name] != None): 
						M1[cols[0]].append(gene_ens[name])

		Go1 = {}
		for key in M1:
			Go1[key] = set()
		lc = 0
		for line in gofile:
			lc = lc+1
			if lc % 1000 == 0:
				print lc
			if line[0] == "!":
				continue
			cols = line.split("\t")
			#if high-level category skip
			if (cols[4] == "GO:0008150" or cols[4] == "GO:0005575" or cols[4] == "GO:0003674"):
				continue;
			found_key = False
			for key in M1:
				for name in M1[key]:
					if name[0:4] == "ENSM":
						if gene_ens[name] != None:
							if gene_ens[name] == cols[2]:
								found_key = True
								break;
					if found_key == True:
						break		
				if found_key == True:
					#GO ID is at cols[4]
					Go1[key].add(cols[4])
					if lc % 1000 == 0:
						print Go1[key]	
					break	
				

		for key in Go1:
			outfile.write('|'.join(M1[key]) + " ")
			outfile.write('|'.join(list(Go1[key])) + "\n")

		outfile.close()
					
if __name__ == "__main__":
	#id_to_name file format:
	#dm10840 CG6612 DIP:22971N
	#at each line where dm10840 is the name used in the ppi network and the rest are assigned names
	#sample run:
	#python pyscripts/go_association.py data/scere_idtoname.txt data/gene_association_scere.sgd data/scere_gene_to_go.txt
	#while in the main folder				
	inputdata = GoAssociation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])		
																					
