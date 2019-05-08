file="resnik_result_iid3.txt"
f1=open(file)
f2=open("formated_"+file,"w")
it=iter(f1)
try:
	while True:
		try:
			f2.write(next(it).rstrip()+"\t"+next(it).rstrip()+"\n")
		except:
			break
finally:

	f1.close()
	f2.close()

