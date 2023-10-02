from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@DB_HOST/hooplogic'
db = SQLAlchemy(app)
