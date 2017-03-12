from app import db

class Fridge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	foods = db.relationship('FoodItem', lazy='dynamic')
	def __repr__(self):
		return '<Fridge %r>' % (self.name)

class FoodItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	calories = db.Column(db.Integer)
	quantity = db.Column(db.Integer)
	fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
	fridge = db.relationship(Fridge)
	def __repr__(self):
		return '<Food %r>' % (self.name)