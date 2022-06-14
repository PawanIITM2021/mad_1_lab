from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabom.sqlite3"


class Section(db.Model):  # db.Model is a class which is inherited by the class section
    section_id = db.Column(db.Integer(), primary_key=True)
    section_name = db.Column(db.String(58), nullable=False)
    books = db.relationship("Book", backref = "section")

    def __repr__(self):
        return "< Section %r>" % self.section_name


class Book(db.Model):
    book_id = db.Column(db.Integer(), primary_key=True)
    book_name = db.Column(db.String(50), nullable=False)
    sect = db.Column(db.Integer(), db.ForeignKey(
        "section.section_id"), nullable=False)
	
    

    def __repr__(self):
          return "< Book %r>" % self.book_name
          
	
	
