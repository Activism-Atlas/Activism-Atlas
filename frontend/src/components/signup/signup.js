import React, { Component } from "react";
import styles from './signup.module.css';

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
            <div className={styles.mainBodyInner}>
            <form onSubmit={(e) => {this.props.handleSignup(e, this.state)}}>
                <h3 className="text-center">Sign Up</h3>

                <div className="form-group">

                    <input type="text" className="form-control" name="first_name" onChange={e => this.handleChange(e)} value={this.state.first_name} placeholder="First name" />
                </div>

                <div className="form-group">

                    <input type="text" className="form-control" name="last_name" onChange={e => this.handleChange(e)} value={this.state.last_name} placeholder="Last name" />
                </div>

                <div className="form-group">

                    <input type="email" className="form-control" name="email" onChange={e => this.handleChange(e)} value={this.state.email} placeholder="Email" />
                </div>

                <div className="form-group">

                    <input type="password" className="form-control" name="password" onChange={e => this.handleChange(e)} value={this.state.password} placeholder="Password" />
                </div>

                <button type="submit" className="btn btn-primary btn-block">Sign Up</button>
                <p className="text-center pt-2">
                    Already registered <a href="#" className="text-primary">login</a>?
                </p>
            </form>
            </div>
        );
    }
}