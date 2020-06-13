import React, { Component } from "react";
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'; // imports bootstrap
import './App.css'; // imports styling, i also have some in Index.css, which shows too
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom"; // this is React Router, it creates routes & links for components 

import Login from "./components/login";
import SignUp from "./components/signup";
import Home from "./components/home";

class App extends Component {
  constructor() {
    super();
    this.state = {
      currentUser: {}, // this is keep tracking of the current user.
    };
  };
  

  handleLoginSubmit = async (event, loginInfo) => {
    event.preventDefault();
    console.log(loginInfo);
    // const fetchUrl = "http://localhost:3000/login";
    // const settings = {
    //   method: "POST",
    //   headers: {
    //     "Content-Type": "application/json",
    //     Accept: "application/json"
    //   },
    //   body: JSON.stringify({
    //     auth: {
    //       user_name: loginInfo.user_name,
    //       password: loginInfo.password
    //     }
    //   })
    // };
    // const response = await fetch(fetchUrl, settings);
    // const postData = await response.json();
    // // console.log(postData)
    // if (!!postData.error === true) return null
    // localStorage.setItem("token", postData.jwt);
    // await this.setState({
    //   currentUser: {
    //     id: Number(postData.user.data.id),
    //     ...postData.user.data.attributes
    //   }
    // })
    
    this.props.history.push("/home")
  };

  handleSignupSubmit = async (event, signupInfo) => {
    event.preventDefault();
    console.log(signupInfo);
    // const fetchUrl = "http://localhost:3000/signup";
    // const settings = {method: "POST",headers: {"Content-Type": "application/json",Accept: "application/json"},
    //   body: JSON.stringify({user: signupInfo})
    // };
    // const response = await fetch(fetchUrl, settings);
    // const postData = await response.json();
    // if (!!postData.error === true) return null
    // console.log(postData.error)
    // localStorage.setItem("token", postData.jwt);
    // this.setState(
    //   {currentUser: {
    //       id: Number(postData.user.data.id),
    //       ...postData.user.data.attributes
    //     }
    //   });
    //   this.props.history.push("/home")
  };


  render(){
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
      <div className="mainBody-div">
        <div className="mainBody-inner">
          <Switch>
          <Route exact path="/" render={(props) => (
              <Login {...props} handleLogin={this.handleLoginSubmit} />)} /> {/* handleLogin passed down to the login, to get the inputed info*/}
            <Route exact path="/login" render={(props) => (
              <Login {...props} handleLogin={this.handleLoginSubmit} />)} />
            <Route exact path="/signup" render={(props) => (
              <SignUp {...props} handleSignup={this.handleSignupSubmit} />)} />  {/* handleSignUp passed down to the login, to get the inputed info*/}
              <Route exact path="/home" component={Home} />
            {/* ^^might not need this */}
          </Switch>
        </div>
      </div>
    </div>
    </Router>
  );
  }
}


export default App;