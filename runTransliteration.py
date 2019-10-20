# -*- coding: utf-8 -*-
import csv
import sys

reader = csv.reader(open('svar.csv', 'r'))
vowels = {}
for row in reader:
	k, v = row
	vowels[k] = v

reader = csv.reader(open('vyanjan.csv', 'r'))
consonants = {}
for row in reader:
	k, v = row
	consonants[k] = v

file = open(sys.argv[1],'r')
content = file.readlines()
file.close()

str1 = ""

for x in content:
	for i in range(len(x)):
		if (i+1<len(x) and x[i+1].strip()==' ़'.strip()):
			c = x[i]+x[i+1]
			p=2
		else:
			c = x[i]
			p=1
		if (c in vowels.keys()):
			str1 = str1 + vowels[c]
		elif (c in consonants.keys()):
			if(i+p<len(x) and x[i+p] in consonants.keys()):
				if(c=='झ' and i!=0) or (c == 'ॠ'): # add 'a' after 'jh', only if झ appears in the starting of the word
					str1 = str1 + consonants[c]
				else:
					str1 = str1 + consonants[c]+'a'
			else:
				str1 = str1 + consonants[c]
		elif x[i] in ['\n','\t',' ','!',',','।','-',':'] or c.isalnum():
			str1 = str1 + c.replace('।','.')

file = open(sys.argv[1]+'OUTPUT','w')
file.write(str1.strip())
file.close()
print("DONE! Open "+sys.argv[1]+"OUTPUT")
