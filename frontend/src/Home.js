import React, { useState, useEffect } from 'react';

const Home = () => {
    const [players, setPlayers] = useState([]);
    const [timeoutFlag, setTimeoutFlag] = useState(null);
    const [inputValue, setInputValue] = useState('');
    let timerId; // Store the timer ID   
    const staticPlayerData = [
      {
        id: 1,
        first_name: "John",
        last_name: "Smith",
        position: "Guard",
        team_id: 22,
      },
      {
        id: 2,
        first_name: "Jane",
        last_name: "Johnson",
        position: "Forward",
        team_id: 40,
      },
      {
        id: 3,
        first_name: "Michael",
        last_name: "Brown",
        position: "Center",
        team_id: 32,
      },
      {
        id: 4,
        first_name: "Emma",
        last_name: "Davis",
        position: "Guard",
        team_id: 51,
      },
      {
        id: 5,
        first_name: "Daniel",
        last_name: "Jones",
        position: "Forward",
        team_id: 12,
      },
      {
        id: 6,
        first_name: "Olivia",
        last_name: "Miller",
        position: "Center",
        team_id: 35,
      },
      {
        id: 7,
        first_name: "William",
        last_name: "Wilson",
        position: "Guard",
        team_id: 22,
      },
      {
        id: 8,
        first_name: "Sophia",
        last_name: "Moore",
        position: "Forward",
        team_id: 50,
      },
      {
        id: 9,
        first_name: "Ethan",
        last_name: "Taylor",
        position: "Center",
        team_id: 16,
      },
      {
        id: 10,
        first_name: "Ava",
        last_name: "Anderson",
        position: "Guard",
        team_id: 2,
      },
      {
        id: 11,
        first_name: "Noah",
        last_name: "Harris",
        position: "Forward",
        team_id: 44,
      },
      {
        id: 12,
        first_name: "Mia",
        last_name: "Martin",
        position: "Center",
        team_id: 37,
      },
      {
        id: 13,
        first_name: "Liam",
        last_name: "Clark",
        position: "Guard",
        team_id: 36,
      },
      {
        id: 14,
        first_name: "Oliver",
        last_name: "Lewis",
        position: "Forward",
        team_id: 49,
      },
      {
        id: 15,
        first_name: "Emma",
        last_name: "Walker",
        position: "Center",
        team_id: 41,
      },
      {
        id: 16,
        first_name: "Isabella",
        last_name: "Young",
        position: "Guard",
        team_id: 28,
      },
      {
        id: 17,
        first_name: "James",
        last_name: "White",
        position: "Forward",
        team_id: 13,
      },
      {
        id: 18,
        first_name: "Benjamin",
        last_name: "King",
        position: "Center",
        team_id: 33,
      },
      {
        id: 19,
        first_name: "Lucas",
        last_name: "Hill",
        position: "Guard",
        team_id: 47,
      },
      {
        id: 20,
        first_name: "Abigail",
        last_name: "Carter",
        position: "Forward",
        team_id: 48,
      },
      {
        id: 21,
        first_name: "Alexander",
        last_name: "Scott",
        position: "Center",
        team_id: 22,
      },
      {
        id: 22,
        first_name: "Avery",
        last_name: "Morris",
        position: "Guard",
        team_id: 17,
      },
      {
        id: 23,
        first_name: "Charlotte",
        last_name: "Turner",
        position: "Forward",
        team_id: 10,
      },
      {
        id: 24,
        first_name: "Jackson",
        last_name: "Adams",
        position: "Center",
        team_id: 11,
      },
      {
        id: 25,
        first_name: "Liam",
        last_name: "Wright",
        position: "Guard",
        team_id: 7,
      },
      {
        id: 26,
        first_name: "Olivia",
        last_name: "Parker",
        position: "Forward",
        team_id: 9,
      },
      {
        id: 27,
        first_name: "Lucas",
        last_name: "Hall",
        position: "Center",
        team_id: 38,
      },
      {
        id: 28,
        first_name: "Sophia",
        last_name: "Mitchell",
        position: "Guard",
        team_id: 1,
      },
      {
        id: 28,
        first_name: "Sophia",
        last_name: "Mitchell",
        position: "Guard",
        team_id: 35,
      },
      {
        id: 29,
        first_name: "Liam",
        last_name: "Baker",
        position: "Forward",
        team_id: 41,
      },
      {
        id: 30,
        first_name: "Ella",
        last_name: "Garcia",
        position: "Center",
        team_id: 20,
      }
    ]    
        const fetchPlayers = (inputValue) => {
          console.log('fetching data for: ', inputValue);

          // Encode the input value to handle special characters
          const encodedInputValue = encodeURIComponent(inputValue);

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

        const checkForTwoChars = (inputValue) => {
          if (inputValue.length >= 2) {
            console.log(`Search for players with at least 2 characters: ${inputValue}`);
            // Clear any previous timers to prevent multiple updates
            clearTimeout(timerId);
            timerId = setTimeout(() => {
              if(timeoutFlag == false){
                setTimeoutFlag(true);
              }
              else if(timeoutFlag == true){
                setTimeoutFlag(false);
              }
              else if(timeoutFlag == null){
                setTimeoutFlag(true);
              }
            }, 1000);
          }
        };
      
        const handleInputChange = (event) => {
          setInputValue(event.target.value);
          checkForTwoChars(inputValue);
        };

        useEffect(() => {
          console.log('timer just ended! The input was:', inputValue);
          if(timeoutFlag != null){
            fetchPlayers(inputValue);
          }
        }, [timeoutFlag])

        return (
          <div className="homePageDiv">
            <div className="homePageLogoDiv">
              <img
                src={process.env.PUBLIC_URL + '/hoopLogicLogo1.png'}
                alt="Hoop Logic Logo"
                className="homePageLogo"
              />
            </div>
            <div className="searchBarDiv">
            <input
              type="text"
              placeholder="Search for players by name"
              className="searchBar"
              style={{ fontFamily: 'Norwester' }}
              onChange={handleInputChange}
            />
            </div>
            <div className='suggestedPlayersBigDiv'>
              <div className="suggestedPlayersDiv">
                  {staticPlayerData.map((player) => (
                    <div key={player.id}>{player.first_name} {player.last_name}</div>
                  ))}
                </div>
                </div>
          </div>
        );
};

export default Home;