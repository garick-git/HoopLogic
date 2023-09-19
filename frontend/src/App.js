import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './Home';
import DeleteMe from './DeleteMe';

function App() {
  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/delete-me-page" element={<DeleteMe />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;