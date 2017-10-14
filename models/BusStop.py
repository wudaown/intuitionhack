import json
import requests
import math

class BusStop:
	def __init__(self, lon,lat,name,line,fake,code):
		self.pos = (lon,lat)
		self.name = name
		self.line = line
		self.fake = fake
		self.code = code



	def addStop(self,lon,lat,name,line,fake,code):
		self.Stop(lon,lat,name,line,fake,code)


	def getPos(self):
		return self.pos

def insert(stop,index,lon,lat,line,fake,code, name):
	stop = stop[:index] + [BusStop(lon,lat,name,line,fake,code)] + stop[index:]
	return stop



def distance(orginPos, destPos, method):
	api_key = 'AIzaSyD-wIj4RjFGgZQriqGlMAdvwS1i2ZOcLYI'
	base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

	origins = [str(orginPos[1]) + ' ' + str(orginPos[0])]
	destinations = [str(destPos[1]) + ' ' + str(destPos[0])]
	# Prepare the request details for the assembly into a request URL
	payload = {
		'origins': '|'.join(origins),
		'destinations': '|'.join(destinations),
		'mode': method,
		'api_key': api_key
	}

	# Assemble the URL and query the web service
	r = requests.get(base_url, params=payload)

	# Check the HTTP status code returned by the server. Only process the response,
	# if the status code is 200 (OK in HTTP terms).
	if r.status_code != 200:
		print('HTTP status code {} received, program terminated.'.format(r.status_code))
	else:
		x = json.loads(r.text)

		# Now you can do as you please with the data structure stored in x.
		# Here, we print it as a Cartesian product.
		for isrc, src in enumerate(x['origin_addresses']):
			for idst, dst in enumerate(x['destination_addresses']):
				row = x['rows'][isrc]
				cell = row['elements'][idst]
			if cell['status'] == 'OK':
				res = cell['distance']['text'].split()
				if res[1] == 'm':
					return float(res[0])
				elif res[1] == 'km':
					return float(res[0]) * 1000
			else:
				return cell['status']

def get_nearest_bus_stop(lon,lat,stops,method):
	mindis = math.inf
	for st in stops:
		if st.fake:
			continue
		try:
			dis = distance((lon,lat),(st.pos[0],st.pos[1]),method)
			if dis < mindis:
				minst = st
		except KeyError:
			print("key not found!")
	return minst

def getStopInfo(stopName, line, redStops, blueStops):
	if line == 'RED':
		for i in redStops:
			print(i.name)
			if stopName == i.name and not i.fake:
				return i
	else:
		for i in blueStops:
			print(i.name)
			if	stopName == i.name and not i.fake:
				return i


def walkTime(orgPos,desPos):
	dis = distance(orgPos,desPos,'walking')
	return 3.6*dis / 5/60
