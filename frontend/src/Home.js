import React from 'react';

const Home = () => {
    return (
        <div className="homePageDiv">
            <div className="homePageLogoDiv">
                <img src='../hoopLogicLogo1.png' alt="Hoop Logic Logo" className="homePageLogo" />
            </div>
            <div className="searchBarDiv">
                <input
                    type="text"
                    placeholder="Player's Name"
                    className="searchBar"
                />
            </div>
        </div>
    );
};

export default Home;
