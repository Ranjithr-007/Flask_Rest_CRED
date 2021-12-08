from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initial DB
db = SQLAlchemy(app)

#Initial Marshmallow
ma = Marshmallow(app)

#Task Class/Model

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

db.create_all()
#Task Schema
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')


#Intial Schema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


#Create a Task

@app.route('/tasks', methods=['Post'])
def create_task():
  title = request.json['title']
  description = request.json['description']

  new_task= Task(title, description)

  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task)
    


#Run Server
if __name__ == "__main__":
    app.run(debug=True)