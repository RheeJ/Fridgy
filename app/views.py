from app import app, models
from flask import request, Response, Flask
from models import *
import json

@app.route('/add', methods=['POST'])
def add_to_fridge():
	data = request.get_json()
	if not hasattr(data['foods'], '__iter__'):
		return Response(status=400)
	fridge = FoodItem.query.filter_by(name=data['fridge'])
	if not fridge.count():
		return Response(status=400)
	for food in data['foods']:
		obj = FoodItem.query.filter_by(name=food['name'], fridge=fridge)
		if not obj.count():
			new_food = models.FoodItem(name=food['name'], calories=food['calories'], quantity=food['quantity'], fridge=fridge)
			db.session.add(new_food)
		else:
			obj.quantity += food['quantity']
	db.session.commit()
	return Response("New Items Have Been Added To Fridge", status=200)

@app.route('/contents', methods=['POST'])
def fridge_content():
	food_list = []
	data = request.get_data()
	fridge = Fridge.query.filter_by(name=data['fridge'])
	if not fridge.count():
		return Response(status=400)
	for food in FoodItem.query.filter_by(fridge=fridge):
		food_list.append({ 'name' : food.name, 'quantity' : food.quantity })
	return Response(json.dumps(food_list), status=200)

	