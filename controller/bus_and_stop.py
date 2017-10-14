import json
from models.BusStop import *
def init_red():
	with open(r"BusStopRed.json", "r") as stop_r:
		stop_red=json.load(stop_r)
	red_line_stops=[]
	Index=1
	for stop in stop_red:
		red_line_stops=insert(red_line_stops, Index, stop["lon"], stop["lat"], "RED", False, stop["code"], stop["title"])
		Index+=1
	red_line_stops=insert(red_line_stops, Index, stop_red[0]["lon"], stop_red[0]["lat"], "RED", False, stop_red[0]["code"], stop_red[0]["title"])
	dist=[]
	for i in range(0, len(red_line_stops)-1):
		dist.append(distance(red_line_stops[i].pos, red_line_stops[i+1].pos))
	return red_line_stops, dist
#red_line_stops, dist=init_red()
#print(dist)
def init_blue():
	blue_line_stops=[]
	dist=[]
	return blue_line_stops, dist

def bus_queue(colour, code):
	ETA=[]
	return ETA