import React, { Component } from "react";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'; // imports bootstrap
// import { BrowserRouter as withRouter,Router, Switch, Route, Link } from "react-router-dom"; // this is React Router, it creates routes & links for components 
import { Route, BrowserRouter as Router, withRouter,Switch, Link} from 'react-router-dom';
import styles from './app.module.css';
import Login from "./components/login/login";
import SignUp from "./components/signup/signup";
import Home from "./components/home/home";

class App extends Component {
  constructor() {
    super();
    this.state = {
      currentUser: {}, // this is keep tracking of the current user.
    };
  };
  

  handleLoginSubmit = async (event, loginInfo) => {
    event.preventDefault();
    const fetchUrl = "http://localhost:8000/auth/token";
    const settings = {method: "POST",headers: { "Content-Type": "application/json", Accept: "application/json"},
      body: JSON.stringify({
          username: loginInfo.username,
          password: loginInfo.password
      })
    };
    const response = await fetch(fetchUrl, settings);
    const postData = await response.json();
    console.log(postData)
    if (!!postData.error === true) return null // we will need to write some logic incase an error comes from the login attempt.
    localStorage.setItem("token", postData.token);
    await this.setState({
      currentUser: {
        username: loginInfo.username
      }
    })
    this.props.history.push("/home") // go to route but doesnt render the component when you login
  };




  render(){
    console.log(this.state)
    console.log(this.props)
  return (
  <Router> 
    {/* Top NavBar Starts here, with the "Activism Atlas" routing to homepage */}
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <Link className="navbar-brand" to={"/home"}>Activism Atlas</Link>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav ml-auto">
              <li className="nav-item">
                <Link className="nav-link" to={"/login"}>Login</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/signup"}>Sign up</Link>
              </li>
            </ul>
          </div>
      </div>
      </nav>
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
               <Route exact path="/home" render={(props) => (
              <Home {...props}  />)} />
            {/* ^^might not need this */}
          </Switch>
          </div>

        </div>


    </Router>
  );
  }
}


export default withRouter(App);