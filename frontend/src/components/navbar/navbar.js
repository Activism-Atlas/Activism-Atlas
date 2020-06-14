import React from "react";
import { Link } from "react-router-dom";
import svg from "./navbarIcon.svg";

function Navbar(props) {
  console.log(props);
  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container mx-0 px-0">
          <Link
            className="navbar-brand d-flex align-contents-center"
            to={"/home"}
          >
            <img src={svg} className="img-fluid mr-2" />
            <h4 className="my-auto">ACTIVISM ATLAS</h4>
          </Link>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav ml-auto">
              {!props.loggedIn ? (
                <>
                  <li className="nav-item">
                    <Link className="nav-link" to={"/login"}>
                      Login
                    </Link>
                  </li>

                  <li className="nav-item">
                    <Link className="nav-link" to={"/signup"}>
                      Sign up
                    </Link>
                  </li>
                </>
              ) : (
                <>
                  <li className="nav-item">
                    <Link
                      onClick={props.handleLogout}
                      className="nav-link"
                      to={"/"}
                    >
                      logout
                    </Link>
                  </li>
                </>
              )}
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default Navbar;
