import os

from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Set Base Directory
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app)
# Setup Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.todoApp')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init Database
db = SQLAlchemy(app)

#Init Marshmallow
marshmallow = Marshmallow(app)

DEBUG = True
PORT = 8000

# @app.route('/')
# def hello_world():
#     return 'Hello World'
@app.route('/todo', methods=['GET'])
@app.route('/todo', methods=['POST'])
@app.route('/todo/<todoid>', methods=['GET', 'DELETE', 'PUT'])
def get_or_create_todo(todoid=None):
    from models import Todo
    if todoid == None and request.method =='GET':
        return Todo.get_todos()
    if todoid == None and request.method=='POST':
        body = request.json['body']
        completed = request.json['completed']
        priority = request.json['priority']
        return Todo.create_todo(body, completed, priority)
    elif todoid != None and request.method == 'GET':
        return Todo.get_todo(todoid)
    elif todoid != None and request.method == 'DELETE':
        return Todo.delete_todo(todoid)
    elif todoid != None and request.method == 'PUT':
        body = request.json['body']
        completed = request.json['completed']
        priority = request.json['priority']

        return Todo.update_todo(todoid, body,completed, priority)
        

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)