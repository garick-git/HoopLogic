db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(10))
    city = db.Column(db.String(50))
    conference = db.Column(db.String(20))
    division = db.Column(db.String(20))
    full_name = db.Column(db.String(100))
    name = db.Column(db.String(50))