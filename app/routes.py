from app import app
from app.controller import UserController

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/users', methods=['GET'])
def users():
    return UserController.index()

@app.route('/users/<id>', methods=['GET'])
def user(id):
    return UserController.show(id)