import React, { Component } from "react";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'; // imports bootstrap
// import { BrowserRouter as withRouter,Router, Switch, Route, Link } from "react-router-dom"; // this is React Router, it creates routes & links for components 
import { Route, BrowserRouter as Router, Redirect, withRouter, Switch} from 'react-router-dom';
import styles from './app.module.css';
import Login from "./components/login/login";
import SignUp from "./components/signup/signup";
import Home from "./components/home/home";
import Navbar from "./components/navbar/navbar";

class App extends Component {
  constructor() {
    super();
    this.state = {
      loggedIn: null, // this is keep tracking of the current user.
    };
  };


  handleLoginSubmit = async (event, loginInfo) => {
    event.preventDefault();
    const fetchUrl = "http://localhost:8000/auth/token";
    const settings = {
      method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify({username: loginInfo.username,password: loginInfo.password})
    };
    const response = await fetch(fetchUrl, settings);
    const postData = await response.json();
    console.log(postData)
    if (!!postData.error === true) return null // we will need to write some logic incase an error comes from the login attempt.
    localStorage.setItem("token", postData.token);
    await this.setState({loggedIn: true})
    this.props.history.push("/home"); // go to route but doesn't render the component when you login
  };

  handleLogout = async () => {
    console.log("clicked")
    localStorage.removeItem("token");
    await this.setState({ loggedIn: false })
    this.props.history.push("/login");
  }



  render() {
    console.log(this.state)
    console.log(this.props)
    return (
      <Router>
        <div className="App">
        {/* Top NavBar Starts here, with the "Activism Atlas" routing to homepage and buttons switch between login and logout*/}
          <Navbar loggedIn={this.state.loggedIn} handleLogout={this.handleLogout} />
          {/* NavBar Ends */}

          {/* Rest of this is the routes: "/", "/login", "/signup" */}
          <div className={styles.mainBodyDiv}>
            <Switch>
              <Route exact path="/" render={(props) => (
                <Login {...props} handleLogin={this.handleLoginSubmit} />)} /> {/* handleLogin passed down to the login, to get the inputed info*/}
              <Route exact path="/login" render={(props) => (
                <Login {...props} handleLogin={this.handleLoginSubmit} />)} />
              <Route exact path="/signup" render={(props) => (
                <SignUp {...props} handleSignup={this.handleSignupSubmit} />)} />  {/* handleSignUp passed down to the login, to get the inputed info*/}
              {(this.state.loggedIn) ? (
                <Route exact path="/home" render={(props) => (
                  <Home {...props} />)} />
              ) : (
                  <Redirect to="/login" />
                )}
            </Switch>
          </div>
        </div>
      </Router>
    );
  }
}


export default withRouter(App);