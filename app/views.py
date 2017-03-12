from app import app, models
from flask import request, Response, Flask
from models import *
import json

@app.route('/add', methods=['POST'])
def add_to_fridge():
	data = request.get_json()
	if not hasattr(data, '__iter__'):
		return Response(status=400)
	for food in data:
		obj = FoodItem.query.filter_by(name=food['name'])
		if not obj.count():
			new_food = models.FoodItem(name=food['name'], calories=food['calories'], quantity=food['quantity'])
			db.session.add(new_food)
		else:
			obj.quantity += food['quantity']
	db.session.commit()
	return Response("New Items Have Been Added To Fridge", status=200)

@app.route('/contents', methods=['GET'])
def fridge_content():
	food_list = []
	for food in FoodItem.query.all():
		food_list.append({ 'name' : food.name, 'quantity' : food.quantity })
	return Response(json.dumps(food_list), status=200)

@app.route('/remove', methods=['POST'])
def remove_from_fridge():
	data = request.get_json()
	if not hasattr(data, '__iter__'):
		return Response(status=400)
	for food in data:
		obj = FoodItem.query.filter_by(name=food['name'])
		if obj.count():
			if food['quantity'] < obj.quantity:
				obj.quantity -= food['quantity']
				db.session.commit()
			elif food['quantity'] == obj.quantity:
				obj.delete()
				db.session.commit()
			else:
				return Response(status=400)
		else:
			return Response(status=400)

	