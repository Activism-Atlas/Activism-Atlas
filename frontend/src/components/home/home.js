import React, { Component } from 'react'
import { Table,Form,Button,Dropdown } from 'react-bootstrap';
import styles from './home.module.css';

export class home extends Component {
  render() {
    return (
      <div className={styles.home}>

        <div className="row mt-5 pt-5">
          <div className="col-6 d-flex">
            <Form inline>
              <Form.Label htmlFor="inlineFormInputName2" srOnly>
                Zip
          </Form.Label>
              <Form.Control
                className="mb-2 mr-sm-2"
                id="formZip"
                placeholder="Zip"
              />
              <Button type="submit" className="mb-2">
                Search
  </Button>
            </Form>܀

          <Dropdown>
              <Dropdown.Toggle variant="success" id="dropdown-basic">
                CAUSES
            </Dropdown.Toggle>

              <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </div>
          
          <div className="col-6 d-flex ">
            <Button type="submit" className="mb-2">
              Add Supporter
        </Button>
            <Button type="submit" className="mb-2">
              Upload?
        </Button>
          </div>


        </div>




      <Table striped bordered hover>
        <thead>
          <tr>
            <th scope="col">ACTIVE</th>
            <th scope="col">NAME</th>
            <th scope="col">PHONE</th>
            <th scope="col">EMAIL</th>
            <th scope="col">LOCATION</th>
            <th scope="col">CAUSES</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>JohnSmith</td>
            <td>Boise, Idahooo</td>
            <td>NYC Coders</td>
            <td>BLM</td>
            <td>created today</td>
            <td>updated today</td>
          </tr>
          <tr>
            <td>MarkSmith</td>
            <td>Boise, Idahooo</td>
            <td>NYC Coders</td>
            <td>BLM</td>
            <td>created today</td>
            <td>updated today</td>
          </tr>
          <tr>
            <td>JaneSmith</td>
            <td>Boise, Idahooo</td>
            <td>NYC Coders</td>
            <td>BLM</td>
            <td>created today</td>
            <td>updated today</td>
          </tr>
        </tbody>
      </Table>
            </div >
        )
  }
}

export default home
