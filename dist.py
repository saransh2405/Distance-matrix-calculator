from googlemaps import GoogleMaps
import os
import math
import csv
import time

all_data = []

def distance_points(lat1,lon1,lat2,lon2):

	radius = 6371 # km
	dlat = math.radians(lat2-lat1)
	dlon = math.radians(lon2-lon1)
	a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = radius * c
	#print d
	return d

myfile = open("googleoutputmatrix.csv", 'a')
wr = csv.writer(myfile,delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)

with open('data.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		row[0] = row[0].strip(',')
		all_data.append(row[0].split(','))


del all_data[0]
print all_data

gmaps = GoogleMaps('gmaps api')
i1 = 0
for i in all_data:
	row = []
	i1 += 1
	if i1 > 78:
		for j in all_data:
			if i == j:
				distance = 0
			else:
				c1 = float(i[1]),float(i[2])
				c2 = float(j[1]),float(j[2])
				dirs = gmaps.directions(c1,c2)
				if not dirs:
					time.sleep(10)
					dirs = gmaps.directions(c1,c2)
					distance = float(dirs['Directions']['Distance']['meters'])
					distance = float(distance/1000)
					d1 = distance_points(float(dirs['Directions']['Routes'][0]['Steps'][0]['Point']['coordinates'][1]),float(dirs['Directions']['Routes'][0]['Steps'][0]['Point']['coordinates'][0]),float(i[1]),float(i[2]))
					d2 = distance_points(float(dirs['Directions']['Routes'][0]['End']['coordinates'][1]),float(dirs['Directions']['Routes'][0]['End']['coordinates'][0]),float(j[1]),float(j[2]))
					distance = distance + d1 + d2
					print i,j
				else:
					distance = float(dirs['Directions']['Distance']['meters'])
					distance = float(distance/1000)
					d1 = distance_points(float(dirs['Directions']['Routes'][0]['Steps'][0]['Point']['coordinates'][1]),float(dirs['Directions']['Routes'][0]['Steps'][0]['Point']['coordinates'][0]),float(i[1]),float(i[2]))
					d2 = distance_points(float(dirs['Directions']['Routes'][0]['End']['coordinates'][1]),float(dirs['Directions']['Routes'][0]['End']['coordinates'][0]),float(j[1]),float(j[2]))
					distance = distance + d1 + d2
					print i,j
			row.append(distance)
		wr.writerow(row)
	else:
		print "running."