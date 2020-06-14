import React, { Component } from "react";
import styles from './login.module.css';

export default class Login extends Component {
    constructor() {
        super();
        this.state = {
            username: "",
            password: "",
        };
    }

    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value })
    }
    render() {
        return (
            <div className={styles.mainBodyInner}>
                <form onSubmit={(e) => { this.props.handleLogin(e, this.state) }}>
                    <h3 className="text-center">Login</h3>
                    <div className="form-group">
                        <input type="username" className="form-control" name="username" onChange={e => this.handleChange(e)} value={this.state.username} placeholder="Username" />
                    </div>
                    <div className="form-group">

                        <input type="password" className="form-control" name="password" onChange={e => this.handleChange(e)} value={this.state.password} placeholder="Password" />
                    </div>
                    <div className="form-group">
                        <div className="custom-control custom-checkbox">
                            <input type="checkbox" className="custom-control-input" id="customCheck1" />
                            <label className="custom-control-label" htmlFor="customCheck1">Remember me</label>
                        </div>
                    </div>
                    <button type="submit" className="btn btn-primary btn-block">Submit</button>
                    <p className="text-center pt-2">
                        Forgot <a href="#" className="text-primary ">password</a>?
                </p>
                </form>
            </div>
        );
    }
}