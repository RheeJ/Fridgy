from app import db

class FoodItem(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	calories = db.Column(db.Integer, index=True)
	def __repr__(self):
		return '<Food %r>' % (self.name)