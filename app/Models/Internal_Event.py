from app.db import db

class InternalEvent(db.Model):
    eid = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    logo_image = db.Column(db.String, nullable=False)
    objective = db.Column(db.String, nullable=False)
    rules = db.Column(db.String, nullable=False)
    phases = db.Column(db.String)
    mentors = db.Column(db.String)
    registration_start = db.Column(db.DataTime(), nullable=False)
    registration_end = db.Column(db.DataTime(), nullable=False)
    event_start = db.Column(db.DataTime(), nullable=False)
    event_end = db.Column(db.DataTime(), nullable=False)
