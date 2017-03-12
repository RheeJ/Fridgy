from app import db

class FoodItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True)
	calories = db.Column(db.Integer)
	quantity = db.Column(db.Integer)
	def __repr__(self):
		return '<Food %r>' % (self.name)