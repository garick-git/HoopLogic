import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import './App.css';
import Home from './Home';
import DeleteMe from './DeleteMe';

function App() {
  const navigate = useNavigate();

  // You can add a function to handle the '/' route redirection
  const redirectToHome = () => {
    navigate('/home');
  };

  return (
    <Router>
      <div className='appDiv'>
        <Routes>
          <Route path="/" element={redirectToHome} />
          <Route path="/home" element={<Home />} />
          <Route path="/delete-me-page" element={<DeleteMe />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
