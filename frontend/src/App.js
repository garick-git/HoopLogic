import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Home from './Home';
import PlayerSearch from './PlayerSearch';
import PlayerList from './PlayerList';
import PlayerStats from './PlayerStats';


function App() {
  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/playersearch" element={<PlayerSearch/>} />
          <Route path="/allplayers" element={<PlayerList/>} />
          <Route path="/" element={<Home/>} />
          <Route path="playerStats/:playerId" element={<PlayerStats/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;