#!/usr/bin/python3.5
import enchant
import unidecode
import unicodedata
dico = enchant.request_dict("fr_FR")

keysDict={}
f = open("dictfr2.txt","r")
fl = f.readlines()
for line in fl:
	if len(line)>3:
		line2 = unicode(line, 'utf-8')
		line3 =  unidecode.unidecode(line2)
		keysDict[line3.replace('\n','')]=True
f.close()


inputFile = open("out.txt","r")
outputFile = open("detected","w+")
fl = inputFile.readlines()
oldProgress=0
nbLines = len(fl)
index = -1
for line in fl:
    line2 = unicode(line, 'utf-8')
    word =  unidecode.unidecode(line2.replace('\n',''))
    index+=1
    found = False
    progress = int(round(index*100/nbLines))
    if progress!=oldProgress:
        print(str(progress)+"% : "+word)
        oldProgress=progress
    for wordLen in range(7, 6, -1):
        for chunkPos in range(0,len(word)-wordLen+1):
            chunk = word[chunkPos:chunkPos+wordLen]
            if chunk in keysDict:
                #print(chunk+" ! -> "+word)
                outputFile.write(word+"\t"+chunk+"\n")
                found = True
                break
        if found:
            break

inputFile.close()
outputFile.close()