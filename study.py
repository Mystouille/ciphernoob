import decimal
import mipSolver as ss
import binascii
import sys

ERROR_VALUE = 999

def extractFloatDataTable(fileName, precision=-1):
	"""Extract a 2D array of floating numbers with format x.yyyyy[E-z] into a 2D array of Decimal (optional: reduced precision)
	fileName: the input file's name (must be in the data folder)
	precision (optional): the number of floating digits (default: max)"""
	numbers = []
	f = open("data/"+fileName,"r")
	for line in f:
		#make sure we work on unicode asap
		decodedLine = line.encode('utf-8').decode('utf-8')
		#list of numbers of the current line
		numberStrList = decodedLine.replace(',','').replace('\n','').strip().split(' ')
		numberList = []
		#process them with numpy.float precision
		for numberStr in numberStrList:
			tempStr = numberStr.strip()
			negative = tempStr[0] == '-'
			if 'E-' in numberStr:
				numberStrDec = numberStr.split('E-')
				tempStr = numberStrDec[0].replace('-','')
				#number of integer digits
				nbIntDigit = len(tempStr.split('.')[0])
				nbNewZeros = int(numberStrDec[1]) - (nbIntDigit - 1)
				#remove floating point and minus sign
				tempStr = tempStr.replace('.','')

				tempStr = "0"*nbNewZeros + tempStr
				tempStr = tempStr[:1]+'.'+tempStr[1:]
				if negative:
					tempStr = '-'+tempStr
			if precision >= 0:
				tempStr = tempStr[:2+(1 if negative else 0)+precision]
			try:
				numberList.append(decimal.Decimal(tempStr))
			except:
				numberList.append(ERROR_VALUE)
		numbers.append(numberList)
	f.close()
	return numbers	

#Get the MIP results to compute
def extractActivatedFile(fileName):
	numbersTable=[]
	f = open(fileName,"r")
	for line in f:
		numbers=[]
		lineStr = line.encode('utf-8').decode('utf-8').replace('\n','')
		lineStr = ''.join(lineStr.split(','))
		for i in range(0,len(lineStr)/16):
			numberStr=lineStr[i*16:i*16+16]
			number = hex(int(numberStr,2))
			numbers.append(number)
		numbersTable.append(numbers)
	f.close()
	return numbersTable

def batchMip(numberTable, syntList, instanceName):
	progress = 0
	resultList=[]
	nbTotal = len(numberTable)
	for idx, numberList in enumerate(numberTable):
		newProgress = int(round(idx*100/nbTotal))
		if progress != newProgress:
			progress = newProgress
			sys.stdout.write("\rMIP Batch {0}%".format(progress))
		#default value
		(activatedList, nbNumberUsed, diff) = [0]*len(numberList), -1, -1
		#run the MIP
		if syntList[idx] != ERROR_VALUE:
			(activatedList, nbNumberUsed, diff) = ss.solve(numberList,syntList[idx])
		#store results
		resultList.append((activatedList, nbNumberUsed, diff))

	sys.stdout.write("\rMIP Batch complete!")
	#write results
	rawActivatedFile = open("results/"+instanceName+"raw.txt","w+")
	activatedFile = open("results/"+instanceName+".txt","w+")
	for (activatedList, nbNumberUsed, diff) in resultList:
		for idx,activated in enumerate(activatedList):
			rawActivatedFile.write(str(activated)+",")
		rawActivatedFile.write("\n")
		activatedFile.write(str(nbNumberUsed)+"\t"+str(diff)+"\n")
	rawActivatedFile.close()
	activatedFile.close()

columnTotalList=[189,148,158,141,142,125,121,100,93,94,80,74,67,50,203,54,37,47,59,52,48,218,50,42,24,32,45,40,36,24,34,34,43,56,68,54,91,74,50,69,217,43,61,77,55,56,32,34,56,123,35,17,212,36,42,39,42,38,47,66,34,32,37,89,42,50,34,39,39,14,22,23,29,54,25,27,16,25,32,31,23,39,168,30,24,123,41,25,24,25,190,19,206,44,35,260,47,42,22,22,28,25,23,28,25,29,73,19,241,28,16,26,30,25,82,42,35,31,23,39,35,114,144,161,32,44,33,41,39,103,28,24,32,38,30,36,84,33,38,47,225,46,142,262,63,39,253,48,100,291,86,59,49,46,73,103,50,42,55,132]

suspiciousColumns=[1,2,3,4,5,15,22,41,53,83,91,93,96,109,123,124,141,143,144,147,150]
columnsDict = {}
for column in suspiciousColumns:
	columnsDict[column]=True

def checkColumnSelection(suspiciousColumns, numberTable, syntList):
	minMaxDiff = 99 #absurdly high number
	idealThreshold = min(columnTotalList)
	for threshold in range(min(columnTotalList),max(columnTotalList)):
		maxDiff = 7
		for lineIdx,numberList in enumerate(numberTable):
			total = 0
			for columnIdx,number in enumerate(numberList):
				columnTotal = columnTotalList[columnIdx]
				if columnTotal >= threshold:
					total += number
			diff = abs(total-syntList[lineIdx])
			if diff!=0:
				maxDiff = min(diff, maxDiff)
		if maxDiff < minMaxDiff:
			idealThreshold = threshold
			minMaxDiff = maxDiff
	print("diff = "+str(minMaxDiff))
	print("threshold ="+str(idealThreshold))

def runFromScratch(numberFile, syntFile, precision=-1):
	if precision < 0:
		numberTable = extractFloatDataTable(numberFile)
		syntTable = extractFloatDataTable(syntFile)
	else:
		numberTable = extractFloatDataTable(numberFile,precision = precision)
		syntTable = extractFloatDataTable(syntFile,precision = precision)

	syntList = list(map(lambda x: x[0], syntTable))
	instanceName = numberFile.split('.')[1] \
		+ '_' + syntFile.split('.')[1] \
		+ (('_p' + str(precision)) if precision >=0 else '')
	batchMip(numberTable, syntList, instanceName)

def lookAtResults(fileName):
	resultTable = extractActivatedFile(fileName)
	for resultLine in resultTable:
		for result in resultLine:
			temp = result.split('x')[0]
			print(bytearray.fromhex(temp).decode())

runFromScratch(numberFile="cmpt1.txt", syntFile="synt1.txt", precision=3)

#lookAtResults("results/3praw.txt")
#checkColumnSelection(suspiciousColumns,numberTable,syntList)

#640 lignes
#160 colonnes
#2^10*100 nombres