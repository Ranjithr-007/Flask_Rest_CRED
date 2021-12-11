# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os
# import datetime
# # from flask_user import User, current_user, login_required, roles_required, UserManager, UserMixin

# from flask import (
#     Flask,
#     render_template
# )

# # Create the application instance
# app = Flask(__name__, template_folder="templates")

# # Create a URL route in our application for "/"
# @app.route('/')
# def home():
#     """
#     This function just responds to the browser ULR
#     localhost:5000/

#     :return:        the rendered template 'home.html'
#     """
#     return render_template('home.html')

# #Init app
# app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))


# # # Class-based application configuration
# # class ConfigClass(object):

# #Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# #Initial DB
# db = SQLAlchemy(app)
 

# #   jane = User(name="Jane", email="Jane@gmail.com",password="fuzzbizz")

# #   john = User(name="John",email="john@gmail.com",password="bizzfuzz")
  
# #   db.session.add(jane)
# #   db.session.add(john)
# #   db.session.commit()

# # def create_app():
# #     """ Flask application factory """
    
# #     # Create Flask app load app.config
# #     app = Flask(__name__)
# #     app.config.from_object(__name__+'.ConfigClass')

# #     # Initialize Flask-BabelEx
# #     babel = Babel(app)

    

# #     class User(db.Model, UserMixin):
# #         __tablename__ = 'users'
# #         id = db.Column(db.Integer, primary_key=True)
# #         active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

#         # User authentication information. The collation='NOCASE' is required
#         # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
#         # email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
#         # email_confirmed_at = db.Column(db.DateTime())
#         # password = db.Column(db.String(255), nullable=False, server_default='')

#         # User information
#         # first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
#         # last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

#         # Define the relationship to Role via UserRoles
#         # roles = db.relationship('Role', secondary='user_roles')

#     # Define the Role data-model
#     # class Role(db.Model):
#     #     __tablename__ = 'roles'
#     #     id = db.Column(db.Integer(), primary_key=True)
#     #     name = db.Column(db.String(50), unique=True)

#     # Define the UserRoles association table
#     # class UserRoles(db.Model):
#     #     __tablename__ = 'user_roles'
#     #     id = db.Column(db.Integer(), primary_key=True)
#     #     user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
#     #     role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

#     # Setup Flask-User and specify the User data-model
#     # user_manager = UserManager(app, db, User)

#     # Create all database tables
#     # db.create_all()

#     # if not User.query.filter(User.email == 'member@example.com').first():
#     #     user = User(
#     #         email='member@example.com',
#     #         email_confirmed_at=datetime.datetime.utcnow(),
#     #         password=user_manager.hash_password('Password1'),
#     #     )
#     #     db.session.add(user)
#     #     db.session.commit()

#     # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
#     # if not User.query.filter(User.email == 'admin@example.com').first():
#     #     user = User(
#     #         email='admin@example.com',
#     #         email_confirmed_at=datetime.datetime.utcnow(),
#     #         password=user_manager.hash_password('Password1'),
#     #     )
#     #     user.roles.append(Role(name='Admin'))
#     #     user.roles.append(Role(name='Agent'))
#     #     db.session.add(user)
#     #     db.session.commit()

#     # # The Home page is accessible to anyone
#     # @app.route('/')
#     # def home_page():
#     #     return render_template_string("""
#     #             {% extends "flask_user_layout.html" %}
#     #             {% block content %}
#     #                 <h2>{%trans%}Home page{%endtrans%}</h2>
#     #                 <p><a href={{ url_for('user.register') }}>{%trans%}Register{%endtrans%}</a></p>
#     #                 <p><a href={{ url_for('user.login') }}>{%trans%}Sign in{%endtrans%}</a></p>
#     #                 <p><a href={{ url_for('home_page') }}>{%trans%}Home Page{%endtrans%}</a> (accessible to anyone)</p>
#     #                 <p><a href={{ url_for('member_page') }}>{%trans%}Member Page{%endtrans%}</a> (login_required: member@example.com / Password1)</p>
#     #                 <p><a href={{ url_for('admin_page') }}>{%trans%}Admin Page{%endtrans%}</a> (role_required: admin@example.com / Password1')</p>
#     #                 <p><a href={{ url_for('user.logout') }}>{%trans%}Sign out{%endtrans%}</a></p>
#     #             {% endblock %}
#     #             """)
    
# #Initial Marshmallow
# ma = Marshmallow(app)

# #Task Class/Model

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(70), unique=True)
#     description = db.Column(db.String(100))
  

#     def __init__(self, title, description,time_date):
#         self.title = title
#         self.description = description
  

# db.create_all()
# #Task Schema
# class TaskSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'description')


# #Intial Schema

# task_schema = TaskSchema()
# tasks_schema = TaskSchema(many=True)


# #Create a Task

# @app.route('/tasks', methods=['Post'])
# def create_task():
#   title = request.json['title']
#   description = request.json['description']
  


#   new_task= Task(title, description, time_date)

#   db.session.add(new_task)
#   db.session.commit()

#   return task_schema.jsonify(new_task)

# #Get All Task
# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#   all_tasks = Task.query.all()
#   result = tasks_schema.dump(all_tasks)
#   return jsonify(result)

# #Get Single Task
# @app.route('/tasks/<id>', methods=['GET'])
# def get_task(id):
#   task = Task.query.get(id)
#   return task_schema.jsonify(task)

# #Update a Task
# @app.route('/tasks/<id>', methods=['PUT'])
# def update_task(id):
#   task = Task.query.get(id)

#   title = request.json['title']
#   description = request.json['description']
  
#   task.title = title
#   task.description = description


#   db.session.commit()

#   return task_schema.jsonify(task)


# #Delete Task
# @app.route('/tasks/<id>', methods=['DELETE'])
# def delete_task(id):
#   task = Task.query.get(id)
#   db.session.delete(task)
#   db.session.commit()
#   return task_schema.jsonify(task)


# # @app.route('/', methods=['GET'])
# # def index():
# #     return jsonify({'message': 'Welcome to my API'})


# #Run Server
# if __name__ == "__main__":
#     app.run(debug=True)