import os
import math
import csv
import time

myfile = open("finaloutputmatrix.csv", 'w+')
wr = csv.writer(myfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

all_data1 = []
all_data2 = []
i = 0
with open('outputmatrix.csv', 'r') as csvfile:
	spamreader1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for rows in spamreader1:
		for row in rows:
			print row
			i += 1
		#row = row.strip(',')
		#all_data1.append(row.split(','))


with open('googleoutputmatrix.csv', 'r') as csvfile:
	spamreader2 = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader2:
		#print row
		#row= row.strip(',')
		print i
		#all_data2.append(row.split(','))