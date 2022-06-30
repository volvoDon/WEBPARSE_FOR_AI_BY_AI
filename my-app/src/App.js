import logo from './logo.svg';
import './App.css';
import React from 'react'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    return (
      <div className='App'>
      <h1>WIKIPEDIA QA PARSER</h1>
      <h3>How To Use:</h3>
      <p>use it you do stuff this is random words. I would want it to be about this long.</p>
      <h2>-------------------------------------------------------------------------------</h2>
      <form onSubmit={this.handleSubmit}>
        <label>
          Input Wiki Title Underscore for Spaces:

          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <table>
        
      </table>
      </div>
    );
  }
}

export default App;
