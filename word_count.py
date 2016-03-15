import csv
import sys
file=open("Output.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
openfile = open("words.txt","w")
for k,v in wordcount.items():
    #print (k, v)
	openfile.write(k+", "+str(v)+"\n")


