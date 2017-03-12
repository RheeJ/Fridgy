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
		obj = FoodItem.query.filter_by(name=food['name'], expiration_date=food['expiration_date'])
		if not obj.count():
			new_food = models.FoodItem(name=food['name'], calories=food['calories'], expiration_date=food['expiration_date'], quantity=0)
			db.session.add(new_food)
		else:
			obj.quantity += 1
	db.session.commit()

	return Response("New Items Have Been Added To Fridge", status=200)
	