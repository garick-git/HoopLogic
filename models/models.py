from flask_sqlalchemy import SQLAlchemy
from database import db


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(10))
    city = db.Column(db.String(50))
    conference = db.Column(db.String(20))
    division = db.Column(db.String(20))
    full_name = db.Column(db.String(100))
    name = db.Column(db.String(50))

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    position = db.Column(db.String(10))
    height_feet = db.Column(db.Integer)
    height_inches = db.Column(db.Integer)
    weight_pounds = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    team = db.relationship('Team', backref='players')

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    home_team_score = db.Column(db.Integer)
    visitor_team_score = db.Column(db.Integer)
    season = db.Column(db.Integer)
    period = db.Column(db.Integer)
    status = db.Column(db.String(20))
    time = db.Column(db.String(20))
    postseason = db.Column(db.Boolean)
    home_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    visitor_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    home_team = db.relationship('Team', foreign_keys=[home_team_id])
    visitor_team = db.relationship('Team', foreign_keys=[visitor_team_id])

class PlayerStats(db.Model):
    __tablename__ = 'player_stats'

    id = db.Column(db.Integer, primary_key=True)
    ast = db.Column(db.Integer)
    blk = db.Column(db.Integer)
    dreb = db.Column(db.Integer)
    fg3_pct = db.Column(db.Float)
    fg3a = db.Column(db.Integer)
    fg3m = db.Column(db.Integer)
    fg_pct = db.Column(db.Float)
    fga = db.Column(db.Integer)
    fgm = db.Column(db.Integer)
    ft_pct = db.Column(db.Float)
    fta = db.Column(db.Integer)
    ftm = db.Column(db.Integer)
    min = db.Column(db.String(10))
    oreb = db.Column(db.Integer)
    pf = db.Column(db.Integer)
    pts = db.Column(db.Integer)
    reb = db.Column(db.Integer)
    stl = db.Column(db.Integer)
    turnover = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    player = db.relationship('Player', backref='player_stats')
    game = db.relationship('Game', backref='player_stats')
    team = db.relationship('Team', backref='player_stats')

class SeasonAverages(db.Model):
    __tablename__ = 'season_averages'

    id = db.Column(db.Integer, primary_key=True)
    games_played = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
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
