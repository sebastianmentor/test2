from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/demo1'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
 
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80), unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    postalcode = db.Column(db.String(10), unique=False, nullable=False)
    favoritmat = db.Column(db.String(20), unique=False, nullable=True)
    favoritfarg = db.Column(db.String(30), unique=False, nullable=True)

if __name__  == "__main__":
    with app.app_context():
        upgrade()
        
        p = Person()
        p.namn = 'Hans'
        p.city = 'Stockholm'
        p.postalcode = '88888'
        p.favoritmat = 'Hamburgare'
        db.session.add(p)
        db.session.commit()