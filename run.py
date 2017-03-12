#!flask/bin/python
import imp
from app import app, db
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
import sys, os

def usage():
	print '-create_db'
	print '-up'
	print '-migrate_db'
if len(sys.argv) != 2:
	usage()
else:
	if sys.argv[1] == '-up':
		app.run(debug=True)
	elif sys.argv[1] == '-create_db':
		db.create_all()
	else:
		usage()