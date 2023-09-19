import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './Home';

function App() {
  return (
      <div className='appDiv'>
          <Home />
      </div>
  );
}

export default App;