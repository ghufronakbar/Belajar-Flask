from app import app
from app.controller import UserController
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return UserController.store()
    else:
        return UserController.index()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def user(id):
    if request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
    return UserController.show(id)