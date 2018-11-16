import argparse

####Fehlermeldung bei mir:

# Traceback (most recent call last):
#   File "D:/Dokumente/Doktorarbeit/scripts/gconv.py", line 92, in <module>
#     f2.write(gconvert(line)+'\n')
#   File "D:/Dokumente/Doktorarbeit/scripts/gconv.py", line 38, in gconvert
#     if inputline[i]==',' :
# IndexError: string index out of range



parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="file with the data to process", type=str)
parser.add_argument("outputfile", help="file where the outputdata is sćomming to be stored", type=str)
parser.add_argument("-w", "--overwritemode", help="if you want to overwrite en existing file, otherwise the script adds just kontext to a existing file", action="store_true")
parser.add_argument("-tr", "--trennung", help="optional seperation in the inputfile, ; has to be written as ';'")
args = parser.parse_args()
if args.overwritemode:
    print("overwriting file")
    writemode = "w"
else:
	writemode = "a"
print (args.trennung)
if args.trennung:
	splitv=args.trennung
else:
	splitv = ";"


inputfile=args.inputfile
outputfile=args.outputfile




#inputline='NS1_1'+';'+'pathogen_EMU_contig_0092:8476-9946'

#outputline='pathogen_EMU_contig_0221	manually_defined	ITR	7740	7968	.	+	.	gene_id "ITR1"; transcript_id "ITR:ITR1"'




def gconvert(inputline):
	if len(inputline)<10 or inputline.find(splitv)==-1:
		return("seperator not found or to short line")
	else:

		# emuj=''
		# chr=''
		# gstart=''
		# gend=''
		sep1='_'
		sep2=splitv
		sep3=':'
		sep4='-'


		emujb=inputline[0:inputline.find(sep1)]
		emujnrb=inputline[inputline.find(sep1):inputline.find(sep2)]
		chrb=inputline[inputline.find(sep2)+1:inputline.find(sep3)]
		gstartb=inputline[inputline.find(sep3)+1:inputline.find(sep4)]
		gendb=str.rstrip(inputline[inputline.find(sep4)+1:len(inputline)])

		# i=0
		# z=len(inputline)
		#
		#
		# while i <= z :
		# 		if inputline[i]=='_' :
		# 			counter=i+1
		# 			i = z
		# 		else :
		# 			emuj=emuj+inputline[i]
		# 		i=i+1
		# emujnr=''
		# i=counter-1
		# z=len(inputline)
		# while i <= z :
		# 		if inputline[i]==splitv:
		# 			counter=i+1
		# 			i = z
		# 		else :
		# 			emujnr=emujnr+inputline[i]
		# 		i=i+1
		#
		# i=counter
		# z=len(inputline)
		# while i <= z :
		# 		if inputline[i]==':' :
		# 			counter=i+1
		# 			i = z
		# 		else :
		# 			chr=chr+inputline[i]
		# 		i=i+1
		#
		#
		#
		# i=counter
		# z=len(inputline)
		# while i <= z :
		# 		if inputline[i]=='-' :
		# 			counter=i+1
		# 			i = z
		# 		else :
		# 			gstart=gstart+inputline[i]
		# 		i=i+1
		#
		#
		# i=counter
		# z=len(inputline)
		# while i <= z-1 :
		# 		gend=gend+str.rstrip(inputline[i]) # macht sonst zeilenumbruch
		# 		i=i+1

		gsumm=int(gstartb)-int(gendb)

		if gsumm<0 :
			gdir='+'
		else :
				gdir='-'
				# zw=gstart
				# gstart=gend
				# gend=zw
				zw=gstartb
				gstartb=gendb
				gendb=zw

		#####\t ist ein tab
		#outputline=chr+'\tmanually_defined\t'+emuj+'\t'+gstart+'\t'+gend+'\t.\t'+gdir+'\t.\tgene_id "'+emuj+emujnr+'"; transcript_id "'+emuj+':'+emuj+emujnr+'.1"'
		outputline2=chrb+'\tmanually_defined\t'+emujb+'\t'+gstartb+'\t'+gendb+'\t.\t'+gdir+'\t.\tgene_id "'+emujb+emujnrb+'"; transcript_id "'+emujb+':'+emujb+emujnrb+'.1"'
		# print(outputline+"\n"+outputline2)
		# if outputline==outputline2 :
		# 	print ('OK')
		# else :
		# 	print ('Error')

		return outputline2



content=[]
def readinput ():
	with open(inputfile, 'r') as f:
		for line in f:
			if len(line)>10:
				content.append(line)
				print("reading line:\t"+line)



def writeoutput():
	with open(outputfile, writemode) as f2:
		for x in content:
			if (len(x)<10) or (x.find(splitv)==-1):
				print("seperator not found or to short line\n"+x)
			else:
				f2.write(gconvert(x)+'\n')
				print('writing line:'+x+'\n')

if args.trennung == '_' or args.trennung == ':' or args.trennung == '-':
	print("chose a better seperator")
else:
	readinput()
	writeoutput()
	print ("\nseperator:"+splitv)
