# Fridgy
Can you make a whole week's meals with the items already in your fridge? Let's find out!

# Setting Up the Development Environment
* ROOT DIR

        virtualenv venv
        pip install -r flask flask-migrate flask-sqlalchemy
    
* FOR WINDOWS: edit activate.bat by adding set "FLASK_APP=run.py"

* ROOT DIR
        
        python run.py -create_db
        flask db init
        flask db migrate -m "name of migration"
        flask db upgrade
