# HoopLogic

**NBA player stats, game by game.** Search for any player, pick how many recent games to look at (1 to 50), optionally filter to games against one opponent, and see points, rebounds, assists, threes, free throws made, and points + rebounds + assists (PRA) charted against the player's average for that stretch.

Built by a team of two as our senior project at St. Edward's University (August 2023 to February 2024).

---

## My role (Garick Mendez)

I built the front end. The line-by-line history is in `git blame`; these are the files I wrote:

- **`frontend/src/Graph.js`**: the D3 bar chart at the heart of the app. Each bar is one game. Bars above the player's average are green and bars below it are red, with a hover tooltip that reads OVER or UNDER the average. It uses D3 scales, axes, and a data join inside React effects, and removes its document-level `mousemove` listener when the component unmounts.
- **`frontend/src/PlayerStats.js`**: the player page. It loads the player's bio, fetches each stat category from the API, and drives the chart from the game-count and opponent selectors.
- **`frontend/src/Home.js`**: the landing page with player search, including team logos in the results.
- **`frontend/src/index.css`** and **`fonts/`**: the site's styling, including the mobile layout.

My teammate **Taha Lewis** built the Flask back end: the MySQL models, the API routes, and the jobs that pull games and box scores from the balldontlie API.

---

## How it works

```
React front end  ──HTTP──▶  Flask API  ──SQLAlchemy──▶  MySQL
                                 │
                                 └──▶  balldontlie API (games and box scores)
```

1. The back end pulls NBA games and per-game player stats from the [balldontlie API](https://www.balldontlie.io/) and stores them in MySQL.
2. The front end calls the Flask API (for example `/api/games/search/points/<player_id>/<games_count>`), which returns the player's average and their per-game values for that stat.
3. `Graph.js` draws one bar per game and colors it against that average.

## Tech stack

| Layer | Tools |
| --- | --- |
| Front end | React 18, React Router, D3.js, CSS |
| Back end | Python, Flask, Flask-SQLAlchemy |
| Database | MySQL |
| Data source | balldontlie REST API |
| Deployment | Gunicorn on a DigitalOcean server |

## Project structure

```
frontend/src/
  Home.js            Landing page and player search
  PlayerStats.js     Player page: bio, stat selectors, chart
  Graph.js           D3 bar chart comparing each game to the average
  PlayerList.js      List of all players
routes/              Flask blueprints (player search, stats, data loading)
backend/src/models/  SQLAlchemy models and balldontlie import jobs
backend/src/databaseRetrieval/  Stat queries used by the API routes
app.py               Flask app entry point
```

## Running locally

You need Python 3.10+, Node.js, a MySQL database, and a free balldontlie API key.

```bash
git clone https://github.com/garick-git/HoopLogic.git
cd HoopLogic

# Back end
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in your own values
set -a; source .env; set +a
python app.py

# Front end (in a second terminal)
cd frontend
npm install
npm start
```

## Configuration

Secrets are read from environment variables, never from the code. See `.env.example`.

| Variable | What it's for |
| --- | --- |
| `DATABASE_URL` | SQLAlchemy connection string for MySQL |
| `SECRET_KEY` | Flask secret key |
| `BALLDONTLIE_API_KEY` | API key for importing games and stats |
