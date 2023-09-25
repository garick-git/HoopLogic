import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Home from './Home';
import PlayerDetails from './PlayerDetails';
import PlayerSearch from './PlayerSearch';
import NBAPlayerInfoPage from './RequestTest'; // Replace with the actual path to your component


function App() {
  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/playersearch" element={<PlayerSearch />} />
          <Route path="/nba-player-info" element={<NBAPlayerInfoPage />} />
          <Route path="/" element={<Home />} />
          <Route path="/player/:playerId" element={<PlayerDetails/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
