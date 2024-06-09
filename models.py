from app import db


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    student_no = db.Column(db.String(20))
    isWin = db.Column(db.Boolean())
