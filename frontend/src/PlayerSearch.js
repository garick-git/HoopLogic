import React, { Component } from 'react';

class PlayerSearch extends Component {
  constructor() {
    super();
    this.state = {
      searchInput: '',
      players: [],
    };
  }

  handleInputChange = (e) => {
    this.setState({ searchInput: e.target.value });
  }

  searchPlayers = () => {
    fetch(`/api/player/search/${this.state.searchInput}`)
      .then(response => response.json())
      .then(data => {
        this.setState({ players: data });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  render() {
    return (
      <div>
        <h1>NBA Player Search</h1>
        <input
          type="text"
          placeholder="Search for players by name"
          value={this.state.searchInput}
          onChange={this.handleInputChange}
        />
        <button onClick={this.searchPlayers}>Search</button>
        <ul>
          {this.state.players.map((player, index) => (
            <li key={index}>{player.full_name}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default PlayerSearch;
