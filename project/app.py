from flask import Flask
from extensions import db
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app

app = create_app()

# If not created create database
with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(debug=True)

