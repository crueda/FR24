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
#data = urllib2.urlopen('http://krk.fr24.com/zones/fcgi/na_ne_all.json').read()


json_data = json.loads(data)
 
featureVector = []
for key, value in json_data.iteritems():
	#print key
	#print value
	try:
		lat = value[1]
		lon = value[2]
		heading = value[3]
		vectorCoordinates = []
		vectorCoordinates.append(lon)
		vectorCoordinates.append(lat)
		new_feature = {}
		new_feature['type'] = 'Feature'
		new_properties = {}
		new_properties['name'] = key
		new_properties['heading'] = heading
		new_geometry = {}
		new_geometry['type'] = 'Point'
		new_geometry['coordinates'] = vectorCoordinates
		new_feature['geometry'] = new_geometry
		new_feature['properties'] = new_properties
		featureVector.append(new_feature)
	except:
		pass

#new_data = {}
#new_data['type'] = 'FeatureCollection'
#new_data['features'] = featureVector
#geojson_data = json.dumps(new_data)
#geojson_data = json.dumps(featureVector)

with open('./html/aviones_all.json', 'w') as outfile:
    #json.dump(new_data, outfile)
    json.dump(featureVector, outfile)

