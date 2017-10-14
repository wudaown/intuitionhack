from flask import  Flask, jsonify
from controller.bus_and_stop import *
from controller.getBusData import *

app = Flask(__name__)

red_stop, red_dist = init_red()
blue_stop, blue_dist = init_blue()

def bus_queue(code,line):
	print(code)
	print(line)
	etas = [
		{
			'id' : 1,
			'eta' : 10
		}
		,
		{	'id' : 2,
			 'eta' : 20
			 }
	]
	return etas

@app.route("/")
def hello():
	return 'hello'

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

stopName = 'Lee Wee Nam Library'

@app.route('/todo/api/v1.0/eta', methods=['GET'])
def ETA(stopName):
	for i in red_stop:
		if (i.name == stopName or i.code == stopName):
			eta = bus_queue(i.code,i.line)
			return jsonify(eta)



@app.route('/todo/api/v1.0/init',methods=['GET'])
def INIT():
	bus = Bus()
	bus.update_response()
	blueBus = bus.get_blue()
	redBus = bus.get_red()
	return jsonify(blueBus,redBus)


yourLocation = [
	{
		"lat" : 1.3478803,
		"lon": 103.687008,
		"destStop" : stopName
	}
]

@app.route('/todo/api/v1.0/gotolocation', methods=['GET'])
def goToLocation():
	flag = False

	while ( not flag):
		for i in red_stop:
			if (yourLocation['destStop'] == i.name):
				line = i.line
				flag = True
				break

		for i in blue_stop:
			if (yourLocation['destStop'] == i.name):
				line = i.line
				flag = True
				break

	if (line == 'RED'):
		nearStop = get_nearest_bus_stop(yourLocation['lon'],yourLocation['lat'],red_stop,'driving')
	else:
		nearStop = get_nearest_bus_stop(yourLocation['lon'],yourLocation['lat'],blue_stop,'driving')

	etaToNear = bus_queue(nearStop.code, nearStop.line)





if __name__ == '__main__':
	app.run(debug=True)
