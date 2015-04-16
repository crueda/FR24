#!/usr/bin/env python
#-*- coding: UTF-8 -*-

# autor: Carlos Rueda
# date: 2015-04-15
# mail: carlos.rueda@deimos-space.com
# version: 1.0

##################################################################################
# version 1.0 release notes:
# Initial version
# Requisites: 
#	library configobj 			To install: "apt-get install python-configobj"
##################################################################################

import time
import sys
import os
import datetime
import logging, logging.handlers
import uuid

import urllib2, json
 
data = urllib2.urlopen('http://krk.fr24.com/zones/fcgi/spain.json').read()
json_data = json.loads(data)
 
#print json_data

#print json_data['60162b0']
featureVector = []
for key, value in json_data.iteritems():
	#print key
	#print value
	try:
		lat = value[1]
		lon = value[2]
		#print lat
		vectorCoordinates = []
		vectorCoordinates.append(lon)
		vectorCoordinates.append(lat)
		new_feature = {}
		new_feature['type'] = 'Feature'
		new_geometry = {}
		new_geometry['type'] = 'Point'
		new_geometry['coordinates'] = vectorCoordinates
		new_feature['geometry'] = new_geometry
		featureVector.append(new_feature)
	except:
		#print "a"
		pass

new_data = {}
new_data['type'] = 'FeatureCollection'
new_data['features'] = featureVector
geojson_data = json.dumps(new_data)

print geojson_data

#for key, value in geojson_data.iteritems():
#	print key
#	print value

'''
import json
json.dumps(['variable', {'lista': ('item1', None, 15.4, 20)}])
print json.dumps({"w": 0, "b": 0, "r": 0}, sort_keys=True)
lista={'a':1,'b':2,'c':3}
json.dumps(lista)

f = open('a.json', 'w')
json.dump(x, f)
'''