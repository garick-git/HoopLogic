import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    // Make an HTTP request to the Python backend
    fetch('/api/data')
      .then(response => response.json())
      .then(result => setData(result))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="App">
      <h1>Hello from React</h1>
      <p>Message from Python: {data.message}</p>
    </div>
  );
}

export default App;
