import os
import math
import csv
import time

myfile = open("outputmatrix.csv", 'w+')
wr = csv.writer(myfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

row = []
all_data = []
id = []
lat = []
lon = []
done_id = []
dist_final = []
one_dist = []
short_list = []
def distance_points(lat1,lon1,lat2,lon2):

	radius = 6371 # km
	dlat = math.radians(lat2-lat1)
	dlon = math.radians(lon2-lon1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = radius * c
	#print d
	return d
	
with open('data.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		row[0] = row[0].strip(',')
		all_data.append(row[0].split(','))

del all_data[0]
for eachdata in all_data:
	id.append(eachdata[0])
	lat.append(eachdata[1])
	lon.append(eachdata[2])
	
all_dist2 = []
for i in range(len(id)):
	all_dist = []
	for j in range(len(id)):
		one_dist = []
		if i is j:
			dist = 0
		else:
			dist = distance_points(float(lat[i]),float(lon[i]),float(lat[j]),float(lon[j]))
		one_dist.append(id[i])
		one_dist.append(id[j])
		one_dist.append(dist)
		#print one_dist
		all_dist.append(one_dist)
	all_dist2.append(all_dist)

#start_point = int(raw_input("Enter the Start Point :"))
#end_point = int(raw_input("Enter the end Point :"))
#print start_point,end_point
#print "direct distance = "
#print str(all_dist2[start_point-1][end_point-1][2])
done_list = []
done_list.append(0)
btw_dist = []
#btw_dist.append(0)
i=0
j=0
while len(done_list) < len(all_dist2[0]):
	max = 10000.000
	#print "new range"
	for j in range(0,len(all_dist2[0])):
		#print j
		if all_dist2[i][j][2] == 0:
			#print "Point is 0"
			t=0
		else:
			if j not in done_list:
		#		print "j="+str(j)
				if all_dist2[int(i)][int(j)][2] < max:
					max  = all_dist2[int(i)][int(j)][2]
					point = int(all_dist2[int(i)][int(j)][1])
					point = point -1
							
	#print i
	i = point
	#print i
	done_list.append(point)
	btw_dist.append(max)
#print btw_dist
#print done_list
#print done_list
final_data = []
new = []
row1 = []
'''
for x in range(len(done_list)):
	for y in range(x,len(done_list)):
		new.append(0)
	final_data.append(new)
'''
#print final_data
for x in range(len(done_list)):
	new = []
	final_data = []
	row1 = []
	for y in range(len(done_list)):

		a = done_list.index(x)
		b = done_list.index(y)
		q = 0.0
		if a == b:
			new.append(0)
		else:
			if a < b:
				for u in range(a,b):
					q += btw_dist[u]
				#print q
				#time.sleep(2)
				new.append(q)
			elif a>b:
				for u in range(b,a):
					q += btw_dist[u]
				#print q
				#time.sleep(2)
				new.append(q)
			else:
				new.append(0)
		#print str(x)+" "+str(y)+" "+str(q)
		e = x+1
		r = y+1
		row1.append(q)

	wr.writerow(row1)