import sys

class IdConverter:
	def __init__(self, id_filename, out_filename):
		outfile = open(out_filename, "w")
		idtoname = open(id_filename)
		
		for line in idtoname:
			cols = line.split()
			for name in cols:
				if name[0:4] == "ENSG":
					outfile.write(name + "\n")

		outfile.close()
					
if __name__ == "__main__":				
	inputdata = IdConverter(sys.argv[1], sys.argv[2])		
																					
