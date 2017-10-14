import requests
'''
bus_color will be a list of json objects
JSON(like python dict) keys
    "lon" - longitude
    "lat" - latitude
    "speed" - speed
    "type" - bus color
    "id" - bus id
    "strange" - bus out of range or strange behavior?
    "angle" - bus direction?
'''

class Bus():
	def __init__(self):
		self.bus_r = []
		self.bus_b = []
		self.bus_g = []
		self.bus_br = []

	def update_response(self):
	self.bus_r = []
	self.bus_b = []
	self.bus_g = []
	self.bus_br = []
	try:
		busResponse = requests.get("http://128.199.230.115:8080/getBusData")
		for bus in busResponse.json():
			if bus["type"] == "Red":
				self.bus_r.append(bus)
			elif bus["type"] == "Blue":
				self.bus_b.append(bus)
			elif bus["type"] == "Brown":
				self.bus_br.append(bus)
			elif bus["type"] == "Green":
				self.bus_g.append(bus)
	except ValueError:
		print("Unable to parse json")
	except KeyError:
		print("No bus type found")
	
	def get_blue(self):
		return self.bus_b
	def get_red(self):
		return self.bus_r

#b = Bus()
#b.update_response()
#print(b.get_red())