import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Home from './Home';
import PlayerSearch from './PlayerSearch';
import InfoPage from './InfoPage';



function App() {
  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/playersearch" element={<PlayerSearch />} />
          <Route path="/" element={<Home />} />
          <Route path="/info" element={<InfoPage/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
