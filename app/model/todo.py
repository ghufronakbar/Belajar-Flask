from app import db
from datetime import datetime
from app.model.user import Users

class Todos (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)    
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id), nullable=False)
    
    def __repr__(self):
        return '<Todo {}>'.format(self.todo)
    