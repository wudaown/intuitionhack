from flask import  Flask, jsonify
import json
from controller.bus_and_stop import init_red, init_blue
from controller.getBusData import Bus

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
def ETA():
	for i in red_stop:
		if (i.name == stopName):
			eta = bus_queue(i.code,i.line)
			return jsonify(eta)



@app.route('/todo/api/v1.0/init',methods=['GET'])
def INIT():
	bus = Bus()
	bus.update_response()
	blueBus = bus.get_blue()
	redBus = bus.get_red()
	return jsonify(blueBus,redBus)



if __name__ == '__main__':
	app.run(debug=True)
