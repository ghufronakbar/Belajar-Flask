from app.model.user import Users
from app import response, app, db
from flask import request

def index():
    try:
        users = Users.query.all()
        data =  transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], "Error")
        
def show(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")
        data =  singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], "Error")
        
def transform(users):
    array = []
    for user in users:
        array.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    return array

def singleTransform(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }
    
def store():
    try:
        data = request.json
        
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        
        if not all([name, email, password]):
            return response.badRequest([], "All fields are required")
        
        check = Users.query.filter_by(email=email).first()
        if check:
            return response.badRequest([], "Email already exists")
        
        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.ok('', 'Successfully created user')
    except Exception as e:
        print(e)
        return response.badRequest('', 'Error')
    
def update(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")
        
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        user.name = name
        user.email = email
        user.setPassword(password)
        db.session.commit()
        
        return response.ok('', 'Successfully updated user')
    except Exception as e:
        print(e)
        return response.badRequest('', 'Error')
    
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "User not found")
        
        db.session.delete(user)
        db.session.commit()
        
        return response.ok('', 'Successfully deleted user')
    except Exception as e:
        print(e)
        return response.badRequest('', 'Error')