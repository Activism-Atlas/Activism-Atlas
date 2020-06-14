import React, { Component } from "react";
import { Table, Form, Button, Dropdown } from "react-bootstrap";
import styles from "./home.module.css";

export class home extends Component {
  render() {
    return (
      <div className={styles.home}>
        <div className="row mb-3 mt-5 pt-5 mx-5">
          <div className="col-6 d-flex">
            <Form inline>
              <Form.Label htmlFor="inlineFormInputName2" srOnly>
                Zip
              </Form.Label>
              <Form.Control
                className="mb-2 mr-sm-1"
                id="formZip"
                placeholder="Zip"
              />
              <Button
                type="submit"
                className="mb-2 mr-4 bg-secondary border-0 text-light"
              >
                Search
              </Button>
            </Form>

            <Dropdown>
              <Dropdown.Toggle
                variant="secondary"
                className="border-0"
                id="dropdown-basic"
              >
                Causes
              </Dropdown.Toggle>

              <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
                <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
                <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </div>

          <div className="col-6 d-flex justify-content-end">
            <Button
              type="submit"
              className="mb-2 bg-secondary border-0 text-light"
            >
              Add Supporter
            </Button>
          </div>
        </div>

        <div className="row mx-5">
          <Table borderless hover>
            <thead className={styles.bgColor}>
              <tr>
                <th scope="col">NAME</th>
                <th scope="col">PHONE</th>
                <th scope="col">EMAIL</th>
                <th scope="col">LOCATION</th>
                <th scope="col">CAUSES</th>
              </tr>
            </thead>
            <tbody>
              <tr className={styles.bgColor}>
                <td>John Smith</td>
                <td>555-123-4567</td>
                <td>email@email.com</td>
                <td>Boise, ID</td>
                <td>
                  BLM, test, test, test, test, test, test, test, test, test,
                  BLM, test, test, test, test, test, test, test, test, test,
                  BLM, test, test, test, test, test, test, test, test, test
                </td>
              </tr>
              <tr className={styles.bgColor}>
                <td>Mark Smith</td>
                <td>555-123-4567</td>
                <td>email@email.com</td>
                <td>Boise, ID</td>
                <td>BLM</td>
              </tr>
            </tbody>
          </Table>
        </div>
      </div>
    );
  }
}

export default home;
