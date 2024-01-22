from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from ..models.player import Player
from database import db

def update_nba_ids():
    # Connect to the database
    engine = create_engine('mysql+mysqlconnector://root:REMOVED@DB_HOST:3306/hooplogic')
    Session = sessionmaker(bind=engine)
    session = Session()


    # Read the CSV file
    csv_file_path = 'NBA_Player_IDs.csv'  # Update with your actual file path
    df = pd.read_csv(csv_file_path)

    # Iterate through each row
    for index, row in df.iterrows():
        # Combine first and last name to match with Player database
        full_name = f"{row['first_name']} {row['last_name']}"

        # Query the Player database to get the player
        player = session.query(Player).filter(or_(Player.first_name == row['first_name'], Player.last_name == row['last_name'])).first()

        # Check if the player is in the database
        if player:
            # Update the NBA_ID attribute in the Player database
            player.nba_id = row['NBAID']

    # Commit the changes to the database
    session.commit()

    # Close the database session
    session.close()
