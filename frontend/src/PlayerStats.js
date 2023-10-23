// routes to call on load: 
// /api/games/search/<player_id>/<games_count
// for local purposes, Stephen Curry will be the object being worked on.

import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

const PlayerStats = () => {
    const { playerId } = useParams();
    const [gameCount, setGameCount] = useState(5);
    const [lastXGames, setLastXGames] = useState(null);
    const [playerData, setPlayerData] = useState(null);
    const [emptySearchBar, setEmptySearchBar] = useState(true);
    const [inputValue, setInputValue] = useState('');
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [players, setPlayers] = useState([]);
    const navigate = useNavigate();
    let timerId; // Store the timer ID 
    const teamLogos = {
      1: 'ATL_Hawks.png',
      2: 'BKN_Nets.png',
      3: 'BOS_Celtics.png',
      4: 'CHA_Hornet.png',
      5: 'CHI_Bulls.png',
      6: 'CLE_Cavaliers.png',
      7: 'DAL_Mavericks.png',
      8: 'DEN_Nuggets.png',
      9: 'DET_Pistons.png',
      10: 'GSW_Warriors.png',
      11: 'HOU_Rockets.png',
      12: 'IND_Pacers.png',
      13: 'LAC_Clippers.png',
      14: 'LAL_Lakers.png',
      15: 'MEM_Grizzlies.png',
      16: 'MIA_Heat.png',
      17: 'MIL_Bucks.png',
      18: 'MIN_Timberwolves.png',
      19: 'NOP_Pelicans.png',
      20: 'NYK_Knicks.png',
      21: 'OKC_Thunder.png',
      22: 'ORL_Magic.png',
      23: 'PHI_76ers.png',
      24: 'PHX_Suns.png',
      25: 'POR_Trailblazers.png',
      26: 'SAC_Kings.png',
      27: 'SAS_Spurs.png',
      28: 'TOR_Raptors.png',
      29: 'UTA_Jazz.png',
      30: 'WAS_Wizards.png',
    };

    const teamNames = {
      1: 'Atlanta Hawks',
      2: 'Brooklyn Nets',
      3: 'Boston Celtics',
      4: 'Charlotte Hornets',
      5: 'Chicago Bulls',
      6: 'Cleveland Cavaliers',
      7: 'Dallas Mavericks',
      8: 'Denver Nuggets',
      9: 'Detroit Pistons',
      10: 'Golden State Warriors',
      11: 'Houston Rockets',
      12: 'Indiana Pacers',
      13: 'LA Clippers',
      14: 'Los Angeles Lakers',
      15: 'Memphis Grizzlies',
      16: 'Miami Heat',
      17: 'Milwaukee Bucks',
      18: 'Minnesota Timberwolves',
      19: 'New Orleans Pelicans',
      20: 'New York Knicks',
      21: 'Oklahoma City Thunder',
      22: 'Orlando Magic',
      23: 'Philadelphia 76ers',
      24: 'Phoenix Suns',
      25: 'Portland Trail Blazers',
      26: 'Sacramento Kings',
      27: 'San Antonio Spurs',
      28: 'Toronto Raptors',
      29: 'Utah Jazz',
      30: 'Washington Wizards',
    };
    
    const localPlayerData = {
      first_name: "Stephen",
      height_feet: 6,
      height_in: 3,
      last_name: "Curry",
      position: "G",
      team_id: 10,
      weight: 190
    };    

    const localLastXGames = [
      {
        date: "Fri, 12 May 2023 00:00:00 GMT",
        home_team: "Los Angeles Lakers",
        home_team_score: 122,
        player_stats: {
          ast: 5,
          blk: 1,
          dreb: 5,
          fg3_pct: 0.285714,
          fg3a: 14,
          fg3m: 4,
          fg_pct: 0.392857,
          fga: 28,
          fgm: 11,
          ft_pct: 1,
          fta: 6,
          ftm: 6,
          min: "39",
          oreb: 1,
          pf: 3,
          pts: 32,
          reb: 6,
          stl: 1,
          turnover: 4
        },
        visitor_team: "Golden State Warriors",
        visitor_team_score: 101
      },
      {
        date: "Wed, 10 May 2023 00:00:00 GMT",
        home_team: "Golden State Warriors",
        home_team_score: 121,
        player_stats: {
          ast: 8,
          blk: 1,
          dreb: 3,
          fg3_pct: 0.272727,
          fg3a: 11,
          fg3m: 3,
          fg_pct: 0.5,
          fga: 24,
          fgm: 12,
          ft_pct: 0,
          fta: 0,
          ftm: 0,
          min: "39",
          oreb: 0,
          pf: 0,
          pts: 27,
          reb: 3,
          stl: 0,
          turnover: 2
        },
        visitor_team: "Los Angeles Lakers",
        visitor_team_score: 106
      },
      {
        date: "Mon, 08 May 2023 00:00:00 GMT",
        home_team: "Los Angeles Lakers",
        home_team_score: 104,
        player_stats: {
          ast: 14,
          blk: 0,
          dreb: 7,
          fg3_pct: 0.214,
          fg3a: 14,
          fg3m: 3,
          fg_pct: 0.4,
          fga: 30,
          fgm: 12,
          ft_pct: 1,
          fta: 4,
          ftm: 4,
          min: "42",
          oreb: 3,
          pf: 5,
          pts: 31,
          reb: 10,
          stl: 3,
          turnover: 2
        },
        visitor_team: "Golden State Warriors",
        visitor_team_score: 121
      },
      {
        date: "Sat, 06 May 2023 00:00:00 GMT",
        home_team: "Los Angeles Lakers",
        home_team_score: 127,
        player_stats: {
          ast: 3,
          blk: 1,
          dreb: 2,
          fg3_pct: 0.4,
          fg3a: 10,
          fg3m: 4,
          fg_pct: 0.428571,
          fga: 21,
          fgm: 9,
          ft_pct: 0.333333,
          fta: 3,
          ftm: 1,
          min: "32",
          oreb: 2,
          pf: 2,
          pts: 23,
          reb: 4,
          stl: 1,
          turnover: 3
        },
        visitor_team: "Golden State Warriors",
        visitor_team_score: 97
      },
      {
        date: "Thu, 04 May 2023 00:00:00 GMT",
        home_team: "Golden State Warriors",
        home_team_score: 127,
        player_stats: {
          ast: 12,
          blk: 0,
          dreb: 4,
          fg3_pct: 0.6,
          fg3a: 5,
          fg3m: 3,
          fg_pct: 0.583333,
          fga: 12,
          fgm: 7,
          ft_pct: 1,
          fta: 3,
          ftm: 3,
          min: "29",
          oreb: 0,
          pf: 3,
          pts: 20,
          reb: 4,
          stl: 1,
          turnover: 3
        },
        visitor_team: "Los Angeles Lakers",
        visitor_team_score: 100
      }
    ];    

    useEffect(() => {
        fetchPlayer(playerId, gameCount);
    }, [])

    const fetchPlayer = (playerId, gameCount) => {
        fetch(`/api/games/search/${playerId}/${gameCount}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then((response) => {
              if (!response.ok) {
                throw new Error('Network response was not ok');
              }
              return response.json();
            })
            .then((data) => {
                setLastXGames(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Stats could not be fetched! Switching to local gamesData...')
              setLastXGames(localLastXGames);
        });

        fetch(`/api/player/search/id/${playerId}`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          })
            .then((response) => {
              if (!response.ok) {
                throw new Error('Network response was not ok');
              }
              return response.json();
            })
            .then((data) => {
              setPlayerData(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Player could not be fetched! Switching to local playerData...')
              setPlayerData(localPlayerData);
        });
    };

    const fetchPlayers = (inputValue) => {
      const encodedInputValue = encodeURIComponent(inputValue); // Encode the input value
    
      // Make the GET request to the backend API
      fetch(`/api/player/search/${encodedInputValue}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then((data) => {
          // Handle the data received from the backend (data may contain player information)
          setPlayers(data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    };
    
      const handleInputChange = (event) => {
        setInputValue(event.target.value);
      };
      
      useEffect(() => {
        if(inputValue.length > 1){
          // Clear any previous timers to prevent multiple updates
          clearTimeout(timerId);
          timerId = setTimeout(() => {
            if(timeoutFlag == false){
              setEmptySearchBar(false)
              setTimeoutFlag(true);
            }
            else if(timeoutFlag == true){
              setEmptySearchBar(false)
              setTimeoutFlag(false);
            }
            else if(timeoutFlag == null){
              setEmptySearchBar(false)
              setTimeoutFlag(true);
            }
          }, 1000);
        }

        else{
          setEmptySearchBar(true);
        }
      }, [inputValue])

      useEffect(() => {
        if(timeoutFlag != null){
          fetchPlayers(inputValue);
        }
      }, [timeoutFlag])

      useEffect(() => {
        console.log('lastXGames: ', lastXGames)
      }, [lastXGames])

      const handleRowClick = (player) => {
        navigate(`/playerStats/${player.id}`);
        window.location.reload();
      };

      return (
        playerData ? (
          <div className='playerStatsPage'>
            <img
              src={process.env.PUBLIC_URL + '/hoopLogicLogo2.png'}
              alt="Hoop Logic Logo"
              id="secondaryLogo"
            />
            <div className='searchBarBigDiv'>
              <div className="searchBarDiv">
                <input
                  type="text"
                  placeholder="Search Again"
                  className="searchBar2"
                  style={{ fontFamily: 'Norwester' }}
                  onChange={handleInputChange}
                />
              </div>
              {emptySearchBar ? null : (
                <div className="suggestedPlayersDiv">
                  <table className='playersTable'>
                    <tbody>
                      {players.map((player) => (
                        <tr className='playersRow' key={player.id} onClick={() => handleRowClick(player)}>
                          <td className="teamLogoCell">
                            <img
                              src={`/teamLogos/${teamLogos[player.team]}`}
                              alt={`Team Logo for Team ${player.team}`}
                              className="teamLogo"
                            />
                          </td>
                          <td className="playerNameCell">{player.first_name} {player.last_name}</td>
                          <td className="playerPositionCell">
                            {player.position === '' ? 'N/A' : player.position === 'G' ? 'Guard' : player.position === 'F' ? 'Forward' : player.position === 'C' ? 'Center' : ''}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
            <div className="pageHeader">
              <img
                src={`/teamLogos/${teamLogos[playerData.team_id]}`}
                alt={`Team Logo for Team ${playerData.team_id}`}
                className="headerLogo"
              />
              <h1 className="playerName">{playerData.first_name} {playerData.last_name}</h1>
            </div>
            <div className="pageContent">
              <div className="biographyDiv">
                <h3 className='biographyTitle'>Bio</h3>
                <table className='biographyTable'>
                  <tbody>
                  <tr className="playerTeam">
                    <p className='playerTeamlbl'>Team: </p>
                    <p className='playerTeamName'>{teamNames[playerData.team_id]}</p>
                  </tr>
                  <tr className="playerPosition">
                      <p className='playerPositionlbl'>Position: </p>
                      <p className="playerPositionName">{playerData ? (
                          playerData.position === 'F'
                            ? 'Forward'
                            : playerData.position === 'C'
                            ? 'Center'
                            : playerData.position === 'G'
                            ? 'Guard'
                            : ''
                        ) : ''}
                      </p>
                  </tr>
                  <tr className="playerHeight">
                      <p className="playerHeightlbl">Height: </p>
                      <p className="playerHeightName">{playerData.height_feet}'{playerData.height_in}"</p>
                  </tr>
                  </tbody>
                </table>
              </div>
              <div className="statsDiv">
                <table className="statsTable">
                  <tbody>
                    <tr>
                      <p>Average Points</p>
                      {/* <p>{lastXGames.}</p> */}
                    </tr>
                    <tr>
                      <td>Row 2, Cell 1</td>
                      <td>Row 2, Cell 2</td>
                    </tr>
                    <tr>
                      <td>Row 3, Cell 1</td>
                      <td>Row 3, Cell 2</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              <div className="graphDiv">
        
              </div>
            </div>
          </div>
        ) : (
          <p>Loading player data...</p>
        )
      );            
}

export default PlayerStats;