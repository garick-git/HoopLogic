// routes to call on load: 
// /api/games/search/<player_id>/<games_count
// for local purposes, Stephen Curry will be the object being worked on.

import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Graph from './Graph.js';

const PlayerStats = () => {
    const { playerId } = useParams();
    
    const [gameCount, setGameCount] = useState(5);
    const [selectedTeam, setSelectedTeam] = useState(1);
    const [playerData, setPlayerData] = useState(null);
    const [emptySearchBar, setEmptySearchBar] = useState(true);
    const [inputValue, setInputValue] = useState('');
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [players, setPlayers] = useState([]);
    const [graphArray, setGraphArray] = useState([]);

    const [pointsArray, setPointsArray] = useState([]);
    const [ftArray, setFtArray] = useState([]);
    const [reboundsArray, setReboundsArray] = useState([]);
    const [threePointersArray, setThreePointersArray] = useState([]);
    const [assistsArray, setAssistsArray] = useState([]);
    const [praArray, setPraArray] = useState([]);

    const [selectedCell, setSelectedCell] = useState(1);
    const navigate = useNavigate();
    let timerId;
    const localDataForPlayers = [{"first_name":"Stephen","id":115,"last_name":"Curry","position":"G","team":10,"total_points":"24477"},
      {"first_name":"Stephen","id":1280,"last_name":"Jackson","position":"F","team":3,"total_points":"12887"},
      {"first_name":"Lance","id":431,"last_name":"Stephenson","position":"G","team":12,"total_points":"5014"},
      {"first_name":"Stephen","id":1655,"last_name":"Graham","position":"","team":11,"total_points":"895"},
      {"first_name":"Jack","id":46395582,"last_name":"Stephens","position":"","team":1,"total_points":"730"},
      {"first_name":"Stephen","id":747,"last_name":"Howard","position":"","team":29,"total_points":"334"},
      {"first_name":"Stephen","id":721,"last_name":"Bardo","position":"","team":27,"total_points":"73"},
      {"first_name":"Everette","id":3079,"last_name":"Stephens","position":"","team":17,"total_points":"65"},
      {"first_name":"Joe","id":1078,"last_name":"Stephens","position":"","team":11,"total_points":"51"},
      {"first_name":"Stephen","id":711,"last_name":"Thompson","position":"","team":22,"total_points":"29"},
      {"first_name":"Stephen","id":2173,"last_name":"Zimmerman","position":"","team":22,"total_points":"19"},
      {"first_name":"DJ","id":430,"last_name":"Stephens","position":"G-F","team":15,"total_points":"9"},
      {"first_name":"Stephen","id":17895907,"last_name":"Domingo","position":"G","team":27,"total_points":"9"}
    ]
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

    const NBA_TEAMS = [
      'All',
      'Atlanta Hawks',
      'Boston Celtics',
      'Brooklyn Nets',
      'Charlotte Hornets',
      'Chicago Bulls',
      'Cleveland Cavaliers',
      'Dallas Mavericks',
      'Denver Nuggets',
      'Detroit Pistons',
      'Golden State Warriors',
      'Houston Rockets',
      'Indiana Pacers',
      'LA Clippers',
      'Los Angeles Lakers',
      'Memphis Grizzlies',
      'Miami Heat',
      'Milwaukee Bucks',
      'Minnesota Timberwolves',
      'New Orleans Pelicans',
      'New York Knicks',
      'Oklahoma City Thunder',
      'Orlando Magic',
      'Philadelphia 76ers',
      'Phoenix Suns',
      'Portland Trail Blazers',
      'Sacramento Kings',
      'San Antonio Spurs',
      'Toronto Raptors',
      'Utah Jazz',
      'Washington Wizards',
    ];

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

    const localGraphArray = {
      points: [26.6, [24, 25, 27, 27, 30, 24, 25, 27, 27, 30,]]
    };

    useEffect(() => {
          fetchPlayer(playerId, gameCount);
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/points/${playerId}/${gameCount}`, {
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
              setPointsArray(data);
              setGraphArray(data);
              console.log('data for points is: ', data)
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setPointsArray(localGraphArray);
          });

          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/FTM/${playerId}/${gameCount}`, {
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
              setFtArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setFtArray(localGraphArray);
          });

          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/rebounds/${playerId}/${gameCount}`, {
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
              setReboundsArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setReboundsArray(localGraphArray);
          });

          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/3PM/${playerId}/${gameCount}`, {
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
              setThreePointersArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setThreePointersArray(localGraphArray);
          });

          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/assists/${playerId}/${gameCount}`, {
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
              setAssistsArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setAssistsArray(localGraphArray);
          });

          fetch(`/api/games/search/PRA/${playerId}/${gameCount}`, {
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
              setPraArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setPraArray(localGraphArray);
          });
    }, [])

    const fetchPlayer = (playerId) => {
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
          setPlayers(localDataForPlayers)
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

      const handleRowClick = (player) => {
        navigate(`/playerStats/${player.id}`);
        window.location.reload();
      };

      const handleGoBack = () => {
        navigate(`/`);
      };

      const handleTeamChange = (selection) => {
        console.log('your team selection: ', selection)
        setSelectedTeam(selection);
      }

      const handleGameCountChange = (selection) => {
        setGameCount(selection);
      }

      const handleCellChange = (selection) => {
        if(selection == 1){ setGraphArray(pointsArray)}
        if(selection == 2){ setGraphArray(ftArray)}
        if(selection == 3){ setGraphArray(reboundsArray)}
        if(selection == 4){ setGraphArray(threePointersArray)}
        if(selection == 5){ setGraphArray(assistsArray)}
        if(selection == 6){ setGraphArray(praArray)}
        setSelectedCell(selection)
      }

      useEffect(() => {
        console.log('selected team: ', selectedTeam, ', selected cell: ', selectedCell, ', # of games: ', gameCount)
        if(selectedTeam != 1){
          if(selectedCell == 1){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/points/${playerId}/${gameCount}/${selectedTeam}`, {
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
                console.log('Points array for last ', gameCount, 'games against opponent ', selectedTeam,': ', data)
                setPointsArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setPointsArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }

          if(selectedCell == 2){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/FTM/${playerId}/${gameCount}/${selectedTeam}`, {
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
                setFtArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setFtArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }

          if(selectedCell == 3){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/rebounds/${playerId}/${gameCount}/${selectedTeam}`, {
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
                setReboundsArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setReboundsArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }

          if(selectedCell == 4){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/3PM/${playerId}/${gameCount}/${selectedTeam}`, {
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
                setThreePointersArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setThreePointersArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }

          if(selectedCell == 5){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/assists/${playerId}/${gameCount}/${selectedTeam}`, {
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
                setAssistsArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setAssistsArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }

          if(selectedCell == 6){
            // Retrieving array of points against a specific team for the last x games
            fetch(`/api/games/search/PRA/${playerId}/${gameCount}/${selectedTeam}`, {
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
                setPraArray(data);
                setGraphArray(data);
              })
              .catch((error) => {
                console.error('Error:', error);
                console.error('Points array could not be fetched! Switching to localGraphArray...')
                setPraArray(localGraphArray);
                setGraphArray(localGraphArray);
            });
          }
      }
      // If the user did not specify a team against:
      else{
      if(selectedCell == 1){
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/points/${playerId}/${gameCount}`, {
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
              setPointsArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setPointsArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }

        if(selectedCell == 2){
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/FTM/${playerId}/${gameCount}`, {
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
              setFtArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setFtArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }

        if(selectedCell == 3){
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/rebounds/${playerId}/${gameCount}`, {
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
              setReboundsArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setReboundsArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }

        if(selectedCell == 4){
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/3PM/${playerId}/${gameCount}`, {
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
              setThreePointersArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setThreePointersArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }

        if(selectedCell == 5){
          // Retrieving array of points against ALL teams for the last x games
          fetch(`/api/games/search/assists/${playerId}/${gameCount}`, {
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
              setAssistsArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setAssistsArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }

        if(selectedCell == 6){
          fetch(`/api/games/search/PRA/${playerId}/${gameCount}`, {
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
              setPraArray(data);
              setGraphArray(data);
            })
            .catch((error) => {
              console.error('Error:', error);
              console.error('Points array could not be fetched! Switching to localGraphArray...')
              setPraArray(localGraphArray);
              setGraphArray(localGraphArray);
          });
        }
      }
      }, [selectedTeam, gameCount, selectedCell])

      useEffect(() => {
        console.log('graphArray has changed to: ', graphArray)
      }, [graphArray])

      return (
        playerData && graphArray ? (
          <div className='playerStatsPage'>
            <img
              src={process.env.PUBLIC_URL + '/hoopLogicLogo2.png'}
              alt="Hoop Logic Logo"
              id="secondaryLogo"
              onClick={handleGoBack}
            />
            <div className='searchBarBigDiv'>
              <div className="searchBarDiv2">
                <input
                  type="text"
                  placeholder="Search Again"
                  className="searchBar2"
                  onChange={handleInputChange}
                />
              </div>
              {emptySearchBar ? null : (
                <div className="suggestedPlayersDiv2">
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
                            {player.position === null ? 'N/A' : player.position === '' ? 'N/A' : player.position === 'G' ? 'Guard' : player.position === 'F' ? 'Forward' : player.position === 'C' ? 'Center' : ''}
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
                        ) : 'N/A'}
                      </p>
                  </tr>
                  <tr className="playerHeight">
                      <p className="playerHeightlbl">Height: </p>
                      <p className="playerHeightName">
                        {playerData.height_feet && playerData.height_in
                          ? `${playerData.height_feet}'${playerData.height_in}"`
                          : 'N/A'}
                      </p>
                  </tr>
                  </tbody>
                </table>
              </div>
              <div className="statsTable">
              <tbody>
              {console.log("pointsArray", pointsArray)}
                {pointsArray && pointsArray.points && pointsArray.points[0] !== undefined && (
                  <div className="pointsCell" onClick={() => handleCellChange(1)}>
                    <p className="pointsLabel">Points</p>
                    <p className="cellNumber" id='pointsNumber'>{pointsArray.points[0]}</p>
                  </div>
                )}

              {console.log("ftArray", ftArray)}
                {ftArray && ftArray.points && ftArray.points[0] !== undefined && (
                  <div className="freeThrowsCell" onClick={() => handleCellChange(2)}>
                    <p className='freeThrowsLabel'>Free Throws</p>
                    <p className='cellNumber'>{ftArray.ftm[0]}</p>
                  </div>
                )}

                {console.log("reboundsArray", reboundsArray)}
                  {reboundsArray && reboundsArray.points && reboundsArray.points[0] !== undefined && (
                    <div className="pointsCell" onClick={() => handleCellChange(3)}>
                      <p className="pointsLabel">Rebounds</p>
                      <p className="cellNumber" id='pointsNumber'>{reboundsArray.rebounds[0]}</p>
                    </div>
                  )}

                {console.log("threePointersArray", threePointersArray)}
                  {threePointersArray && threePointersArray.points && threePointersArray.points[0] !== undefined && (
                    <div className="freeThrowsCell" onClick={() => handleCellChange(4)}>
                      <p className='freeThrowsLabel'>Three Pointers</p>
                      <p className='cellNumber'>{threePointersArray.threepm[0]}</p>
                    </div>
                  )}

                {console.log("assistsArray", assistsArray)}
                  {assistsArray && assistsArray.points && assistsArray.points[0] !== undefined && (
                    <div className="alternateCell1" onClick={() => handleCellChange(5)}>
                      <p className="pointsLabel">Assists</p>
                      <p className="cellNumber" id='pointsNumber'>{assistsArray.assists[0]}</p>
                    </div>
                  )}

                {console.log("praArray", praArray)}
                  {praArray && praArray.points && praArray.points[0] !== undefined && (
                    <div className="alternateCell2" onClick={() => handleCellChange(6)}>
                      <p className='freeThrowsLabel' id='PRALabel'>P+R+A</p>
                      <p className='cellNumber'>{praArray.points[0]}</p>
                    </div>
                  )}
              </tbody>
            </div>

              <div className="graphDiv">
                {graphArray && <Graph graphArray={graphArray} />}
              </div>
            </div>
          </div>
        ) : (
          <p>Loading player data...</p>
        )
      );            
}

export default PlayerStats;