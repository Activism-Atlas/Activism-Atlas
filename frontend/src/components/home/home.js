import React from "react";
import { Table, Form, Button, Dropdown } from "react-bootstrap";
import { Link } from "react-router-dom";
import styles from "./home.module.css";

function home(props) {
  // console.log(props.supporters)

  const table = props.supporters.map((supporter) => {
    console.log(supporter.causes.map((cause) => cause.name));
    return (
      <tr className={styles.bgColor}>
        <td>Yes</td>
        <td>
          {supporter.first_name}, {supporter.last_name}
        </td>
        <td>{supporter.phonenumber}</td>
        <td>{supporter.email}</td>
        <td>
          {" "}
          {supporter.address.city}, {supporter.address.state}
        </td>
        <td>
          {supporter.causes.map(
            (cause, index) => (index ? ", " : "") + cause.name
          )}
        </td>
        {/* <td> </td>
            <td>created today</td>
            <td>updated today</td> */}
      </tr>
    );
  });

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

      <div className="mx-4">
        <Table borderless hover className={styles.bgColor}>
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
          <tbody>{table}</tbody>
        </Table>
      </div>
    </div>
  );
}
export default home;
