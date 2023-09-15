import React, { useState, useEffect } from 'react';

const Home = () => {
    const [inputName, setInputName] = useState(''); 
    const [names, setNames] = useState([]); 
    const [showGreeting, setShowGreeting] = useState(false);

    const handleSubmit = () => {
        const userInput = { name: inputName };
        fetch('http://localhost:3001/names', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userInput),
        })
        setInputName('');
        fetchNames();
        setShowGreeting(true);
    }

    const fetchNames = () => {
        fetch('http://localhost:3001/names')
        .then(response => response.json())
        .then(data => {
            setNames(data);
        })
    }

    return (
        <div className="homePageDiv bg-dark text-light p-4">
            <center>
                <input
                    className="homePageInput"
                    placeholder="enter your name"
                    value={inputName}
                    onChange={(e) => setInputName(e.target.value)}
                /><br />
                <button id="homePageSubmitButton" onClick={handleSubmit}>
                    Submit
                </button>
            </center>

            {showGreeting && (
                <div>
                    <p>Hello, World</p>
                        <table>
                            <tbody>
                                {names.map((name) => 
                                (
                                <tr>
                                    <td>Hello, {name.name}</td>
                                </tr>
                                ))}
                            </tbody>
                        </table>
                </div>
            )}
        </div>
    );
}

export default Home;