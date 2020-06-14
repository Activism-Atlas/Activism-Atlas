import React, { Component } from "react";
import { Link } from "react-router-dom";
import styles from './newsupporter.module.css';
import { Form, Col } from 'react-bootstrap';

export default class NewSupporter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      // NOTE Use below when we start fetching districts from API?
      // error: null,
      // isLoaded: false,
      // districts: [],
      supporter: {
        first_name: '',
        last_name: '',
        email: '',
        phonenumber: '',
        address: {
          street: '',
          city: '',
          zipcode: '',
          state: '',
          district: {
            tag: '',
            name: ''
          }
        },
        causes: []
      }
    };
  }

  // NOTE Getting a 401 unauthorized at this endpoint, is it fully set up?
  // componentDidMount() {
  //   fetch("http://localhost:8000/api/districts")
  //     .then(res => res.json())
  //     .then(
  //       (result) => {
  //         this.setState({
  //           isLoaded: true,
  //           districts: result
  //         })
  //       },
  //       (error) => {
  //         this.setState({
  //           isLoaded: true,
  //           error
  //         })
  //       }
  //     )
  // }

  handleChange = (e) => {
    const { supporter } = { ...this.state }
    const currentState = supporter
    const { name, value } = e.target
    currentState[name] = value

    this.setState({ supporter: currentState })

  }

  handleAddressChange = (e) => {
    const { address } = { ...this.state.supporter }
    const currentState = address
    const { name, value } = e.target
    currentState[name] = value
    this.setState({ address: currentState })
  }

  createSupporter = (e) => {
    e.preventDefault()
    console.log(this.state)
  }

  render() {
    // NOTE Use the code below to fetch districts from API?
    // const { error, isLoaded, districts } = this.state
    // if (error) {
    //   return <div>Error: {error.message}</div>
    // } else if (!isLoaded) {
    //   return <div>Loading...</div>
    // } else {
    // NOTE Inject return statement/JSX in here.
    // }
    return (
      <div className={styles.mainBodyInner}>

        <h3 className="text-center mb-3">Add a Supporter</h3>

        <form onSubmit={(e) => { this.createSupporter(e) }}>
          {/* Row for supporter name */}
          <div className="row">
            <div className="col">
              {/* Supporter's first name */}
              <div className="form-group">
                <input type="text" className="form-control" name="first_name" onChange={e => this.handleChange(e)} value={this.state.supporter.first_name} placeholder="First name" />
              </div>
              {/* End of input field */}
            </div>
            <div className="col">
              {/* Supporter's last name */}
              <div className="form-group">
                <input type="text" className="form-control" name="last_name" onChange={e => this.handleChange(e)} value={this.state.supporter.last_name} placeholder="Last name" />
              </div>
              {/* End of input field */}
            </div>
          </div>

          {/* Email address */}
          <div className="form-group">
            <input type="email" className="form-control" name="email" onChange={e => this.handleChange(e)} value={this.state.supporter.email} placeholder="Email" />
          </div>
          {/* End of input field */}
          {/* Email Address */}
          <div className="form-group">
            <input type="text" className="form-control" name="phonenumber" onChange={e => this.handleChange(e)} value={this.state.supporter.phonenumber} placeholder="Phone Number" />
          </div>
          {/* End of input field */}
          {/* Supporter Address  */}
          <h5 className="text-center">Address</h5>
          <Form.Row>
            <Col xs={9}>
              {/* Street Address */}
              <div className="form-group">
                <input type="text" className="form-control" name="street" onChange={e => this.handleAddressChange(e)} value={this.state.supporter.address.street} placeholder="Street Address" />
              </div>
              {/* End of input field */}
            </Col>
            <Col>
              {/* Zip Code */}
              <div className="form-group">
                <input type="text" className="form-control" name="zipcode" onChange={e => this.handleAddressChange(e)} value={this.state.supporter.address.zipcode} placeholder="05118" />
              </div>
              {/* End of input field */}
            </Col>
          </Form.Row>

          <Form.Row>
            <Col>
              {/* Supporter's city */}
              <div className="form-group">
                <input type="text" className="form-control" name="city" onChange={e => this.handleAddressChange(e)} value={this.state.supporter.address.city} placeholder="City" />
              </div>
              {/* End of input field */}
            </Col>
            <Col xs={3}>
              {/* Supporter's state */}
              <div className="form-group">
                <Form.Control as="select" name="state" onChange={e => this.handleAddressChange(e)} value={this.state.supporter.address.state}>
                  <option value="AL">AL</option>
                  <option value="AK">AK</option>
                  <option value="AZ">AZ</option>
                  <option value="AR">AR</option>
                  <option value="CA">CA</option>
                  <option value="CO">CO</option>
                  <option value="CT">CT</option>
                  <option value="DE">DE</option>
                  <option value="FL">FL</option>
                  <option value="GA">GA</option>
                  <option value="HI">HI</option>
                  <option value="ID">ID</option>
                  <option value="IL">IL</option>
                  <option value="IN">IN</option>
                  <option value="IA">IA</option>
                  <option value="KS">KS</option>
                  <option value="KY">KY</option>
                  <option value="LA">LA</option>
                  <option value="ME">ME</option>
                  <option value="MD">MD</option>
                  <option value="MA">MA</option>
                  <option value="MI">MI</option>
                  <option value="MN">MN</option>
                  <option value="MS">MS</option>
                  <option value="MO">MO</option>
                  <option value="MT">MT</option>
                  <option value="NE">NE</option>
                  <option value="NV">NV</option>
                  <option value="NH">NH</option>
                  <option value="NJ">NJ</option>
                  <option value="NM">NM</option>
                  <option value="NY">NY</option>
                  <option value="NC">NC</option>
                  <option value="ND">ND</option>
                  <option value="OH">OH</option>
                  <option value="OK">OK</option>
                  <option value="OR">OR</option>
                  <option value="PA">PA</option>
                  <option value="RI">RI</option>
                  <option value="SC">SC</option>
                  <option value="SD">SD</option>
                  <option value="TN">TN</option>
                  <option value="TX">TX</option>
                  <option value="UT">UT</option>
                  <option value="VT">VT</option>
                  <option value="VA">VA</option>
                  <option value="WA">WA</option>
                  <option value="WV">WV</option>
                  <option value="WI">WI</option>
                  <option value="WY">WY</option>
                </Form.Control>
              </div>
              {/* End of input field */}
            </Col>
          </Form.Row>
          {/* District Dropdown */}
          {/* NOTE We will need to iterate over api/districts to populate this dropdown */}
          <Form.Control as="select" name="district" onChange={e => this.handleAddressChange(e)}>
            <option value="1">District 1</option>
            <option value="2">District 2</option>
            <option value="3">District 3</option>
            <option value="4">District 4</option>
            <option value="5">District 5</option>
            <option value="6">District 6</option>
          </Form.Control>
          {/* End of input field */}
          {/* Checkboxes for Causes */}
          <div className="mt-3 ml-3">
            <Form.Row>
              <Col xs={6} >
                <Form.Check inline label="Black Lives Matter" type='checkbox' />
                <Form.Check inline label="Police Reform" type='checkbox' />
              </Col>
              <Col xs={6} >
                <Form.Check inline label="Close Rikers" type='checkbox' />
                <Form.Check inline label="Gerrymandering" type='checkbox' />
              </Col>
            </Form.Row>
          </div>
          {/* End of input field */}
          <button type="submit" className="mt-3 btn btn-primary btn-block">Add Supporter</button>
        </form>
      </div>
    );

  }
}