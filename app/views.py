from app import app
from flask import request, Response, Flask
from models import *
import json

@app.route('/add', methods=['POST'])
def add_to_fridge():
	data = request.get_json()
	if not hasattr(data, '__iter__'):
		return Response(status=400)
	for food in data:
		if not FoodItem.query.filter_by(name=food['name']).count():
			new_food = models.FoodItem(name=food['name'], calories=food['calories'])
			db.session.add(new_food)
	db.session.commit()

	return Response("New Items Have Been Added To Fridge", status=200)
	