import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Home from './Home';
import PlayerSearch from './PlayerSearch';
import PlayerList from './PlayerList';



function App() {
  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/playersearch" element={<PlayerSearch />} />
          <Route path="/allplayers" element={<PlayerList />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
