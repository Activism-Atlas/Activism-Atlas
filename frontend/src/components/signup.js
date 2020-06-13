import React, { Component } from "react";

export default class SignUp extends Component {
    constructor() {
        super();
    
        this.state = {
          first_name: "",
          last_name: "",
          email: "",
          password: ""
        };
      }

      handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value})
      }

    render() {
        return (
            <form onSubmit={(e) => {this.props.handleSignup(e, this.state)}}>
                <h3>Sign Up</h3>

                <div className="form-group">
                    <label>First name</label>
                    <input type="text" className="form-control" name="first_name" onChange={e => this.handleChange(e)} value={this.state.first_name} placeholder="First name" />
                </div>

                <div className="form-group">
                    <label>Last name</label>
                    <input type="text" className="form-control" name="last_name" onChange={e => this.handleChange(e)} value={this.state.last_name} placeholder="Last name" />
                </div>

                <div className="form-group">
                    <label>Email address</label>
                    <input type="email" className="form-control" name="email" onChange={e => this.handleChange(e)} value={this.state.email} placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" name="password" onChange={e => this.handleChange(e)} value={this.state.password} placeholder="Enter password" />
                </div>

                <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
                <p className="forgot-password text-right">
                    Already registered <a href="#">login?</a>
                </p>
            </form>
        );
    }
}