from datetime import datetime
from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(100))
    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    views = db.Column(db.Integer, default=0)
    last_viewed = db.Column(db.DateTime)

    def __repr__(self):
        return f"Task('{self.name}', '{self.description}')"
