import logging
from flask import Flask, jsonify
from routes.databasePopulation_BP import databasePopulate_BP
from routes.playerRetrieval_BP import databaseRetrieval_BP
from routes.statRetrieval_BP import statRetrieval_BP
from database import db


app = Flask(__name__)

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)

app.config['SECRET_KEY'] = 'SuperSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:REMOVED@DB_HOST:3306/hooplogic'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(databasePopulate_BP)
app.register_blueprint(databaseRetrieval_BP)
app.register_blueprint(statRetrieval_BP)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
