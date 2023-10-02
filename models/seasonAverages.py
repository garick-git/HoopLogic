from .player import Player
from database import db

class SeasonAverages(db.Model):
    __tablename__ = 'season_averages'

    id = db.Column(db.Integer, primary_key=True)
    games_played = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    season = db.Column(db.Integer)
    min = db.Column(db.String(10))
    fgm = db.Column(db.Float)
    fga = db.Column(db.Float)
    fg3m = db.Column(db.Float)
    fg3a = db.Column(db.Float)
    ftm = db.Column(db.Float)
    fta = db.Column(db.Float)
    oreb = db.Column(db.Float)
    dreb = db.Column(db.Float)
    reb = db.Column(db.Float)
    ast = db.Column(db.Float)
    stl = db.Column(db.Float)
    blk = db.Column(db.Float)
    turnover = db.Column(db.Float)
    pf = db.Column(db.Float)
    pts = db.Column(db.Float)
    fg_pct = db.Column(db.Float)
    fg3_pct = db.Column(db.Float)
    ft_pct = db.Column(db.Float)
    player = db.relationship('Player', backref='season_averages')