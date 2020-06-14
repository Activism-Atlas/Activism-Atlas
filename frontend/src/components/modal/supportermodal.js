import React, { Component } from "react";
import { Button, Modal } from 'react-bootstrap';
import NewSupporter from "../newsupporter/newsupporter"

export default class SupporterModal extends Component {

  SupporterModal = () => {
    const [show, setShow] = React.useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    return (
      <>
        <Button type="submit"
          className="mb-2 bg-secondary border-0 text-light" onClick={handleShow}>
          Add Supporter
        </Button>

        <Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>

          </Modal.Header>
          <Modal.Body>
            <NewSupporter></NewSupporter>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
          </Button>

          </Modal.Footer>

        </Modal>
      </>
    );
  }

  render() {
    return (
      <this.SupporterModal />
    )
  }

}