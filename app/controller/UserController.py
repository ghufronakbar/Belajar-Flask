from app.model.user import Users
from app import response, app

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