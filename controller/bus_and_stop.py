import json
from models.BusStop import *
from controller.getBusData import *
def init_red():
	with open(r"BusStopRed.json", "r") as stop_r:
		stop_red=json.load(stop_r)
	red_line_stops=[]
	Index=1
	for stop in stop_red:
		red_line_stops=insert(red_line_stops, Index, stop["lon"], stop["lat"], "RED", False, stop["code"], stop["title"])
		Index+=1
	red_line_stops=insert(red_line_stops, Index, stop_red[0]["lon"], stop_red[0]["lat"], "RED", False, stop_red[0]["code"], stop_red[0]["title"])
	with open(r"mapdelta.json", "r") as fake_r:
		fake_stop_red=json.load(fake_r)
	Index=0
	prev_str=""
	Code=-1
	for fake_stop in fake_stop_red:
		#print(fake_stop)
		if fake_stop["title"][:-1]!=prev_str:
			Index+=1
		red_line_stops=insert(red_line_stops, Index, fake_stop["lon"], fake_stop["lat"], "RED", True, Code, fake_stop["title"])
		Code-=1
		prev_str=fake_stop["title"][:-1]
		Index+=1
	dist=[]
	for i in range(0, len(red_line_stops)-1):
		dist.append(distance(red_line_stops[i].pos, red_line_stops[i+1].pos))
	for stop in red_line_stops:
		print(stop.name, stop.fake, stop.code)
	return red_line_stops, dist
#red_line_stops, dist=init_red()
#print(dist)
def init_blue():
	blue_line_stops=[]
	dist=[]
	return blue_line_stops, dist

def bus_queue(colour, code):
	ETA=[]
	'''
	if colour=="RED":
		b=Bus()
		b.update_response()
		bus=b.get_red()
		for buses in bus:
	'''
	return ETA