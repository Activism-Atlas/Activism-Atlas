import React, { Component } from "react";

export default class Login extends Component {
    constructor() {
        super();
        this.state = {
          username: "",
          password: "",
        };
      }

      handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value})
      }
    render() {
        return (
            <form onSubmit={(e) => {this.props.handleLogin(e, this.state)}}>
                <h3>Login In</h3>

                <div className="form-group">
                    <label>username address</label>
                    <input type="username" className="form-control" name="username" onChange={e => this.handleChange(e)} value={this.state.username} placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" name="password" onChange={e => this.handleChange(e)} value={this.state.password} placeholder="●●●●●●●"/>
                </div>

                <div className="form-group">
                    <div className="custom-control custom-checkbox">
                        <input type="checkbox" className="custom-control-input" id="customCheck1" />
                        <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                    </div>
                </div>

                <button type="submit" className="btn btn-primary btn-block">Submit</button>
                <p className="forgot-password text-right">
                    Forgot <a href="#">password?</a>
                </p>
            </form>
        );
    }
}