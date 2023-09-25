// Import axios (if not already imported)
import axios from 'axios';

// Define the NBA API endpoint you want to access
const apiUrl = 'https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544';

// Make an HTTP GET request to the NBA API
axios.get(apiUrl)
  .then((response) => {
    // Handle the API response data here
    console.log(response.data);
  })
  .catch((error) => {
    // Handle errors, e.g., network issues or API errors
    console.error('Error fetching NBA data:', error);
  });
