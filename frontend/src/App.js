import React, { Component } from "react";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'; // imports bootstrap
import { Route, BrowserRouter as Router, Redirect, withRouter, Switch } from 'react-router-dom';
import styles from './app.module.css';
import Login from "./components/login/login";
import Home from "./components/home/home";
import Navbar from "./components/navbar/navbar";

class App extends Component {
  constructor() {
    super();
    this.state = {
      loggedIn: null, // this is keep tracking of the current user.
      supporters: []
    };
  };

  handleLoginSubmit = async (event, loginInfo) => {
    event.preventDefault();
    try {
      const fetchUrl = "http://localhost:8000/auth/token";
      const settings = {
        method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({username: loginInfo.username,password: loginInfo.password})
      };
      const response = await fetch(fetchUrl, settings);
      if (!response.ok) {
        throw new Error('Invalid Login');
      }
      const postData = await response.json();
      localStorage.setItem("token", postData.token);
      this.fetchSupporters()
      this.setState({loggedIn: true});
    }
    catch(e) {
      console.log(e.message);
    }
  };

  handleLogout = async () => {
    localStorage.removeItem("token");
    await this.setState({ loggedIn: false })
  }

  fetchSupporters = async () => {
    let fetchUrl = "http://localhost:8000/api/supporters/"
    let token = localStorage.getItem("token")
    let settings = {
      method: "GET", headers: { "Content-Type": "application/json", Accept: "application/json", Authorization: `Bearer ${token}` }
    };
    let response = await fetch(fetchUrl, settings);
    let apiData = await response.json();
    this.setState({
      supporters: apiData
    })
  }

  // handleSupporterSubmit = async (event, supporterInfo) => {
  //   const [first_name,
  //     last_name,
  //     email,
  //     phonenumber,
  //     address,
  //     causes] = supporterInfo;
  //   event.preventDefault();
  //   try {
  //     const fetchUrl = "http://localhost:8000/api/supporters/";
  //     let token = localStorage.getItem("token")
  //     const settings = {
  //       method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json", Authorization: `Bearer ${token}` },
  //       body: JSON.stringify({
  //         first_name,
  //         last_name,
  //         email,
  //         phonenumber,
  //         address,
  //         causes
  //       })
  //     };
  //     const response = await fetch(fetchUrl, settings);
  //     if (!response.ok) {
  //       throw new Error('Invalid supporter information');
  //     }
  //     const postData = await response.json();
  //     this.setState({ supporters: postData, ...this.state });
  //   }
  //   catch (e) {
  //     console.log(e.message);
  //   }
  // };


  render() {
    return (
      <Router>
        <div className="App">
          {/* Top NavBar Starts here, with the "Activism Atlas" routing to homepage and buttons switch between login and logout*/}
          <Navbar loggedIn={this.state.loggedIn} handleLogout={this.handleLogout} />
          <div className={styles.mainBodyDiv}>
            <Switch>
              <Route exact path="/" render={(props) => (
                <Login {...props} handleLogin={this.handleLoginSubmit} />)} /> {/* handleLogin passed down to the login, to get the inputed info*/}
              <Route exact path="/login" render={(props) => (
                <Login {...props} handleLogin={this.handleLoginSubmit} />)} />
              <Route exact path="/home" render={(props) => (
                <Home {...props} supporters={this.state.supporters} handleSupporterSubmit={this.handleSupporterSubmit}/>)} />
            </Switch>
            {(!this.state.loggedIn) ? <Redirect to="/login" /> : <Redirect to="/home" />}
          </div>
        </div>
      </Router>
    );
  }
}


export default withRouter(App);