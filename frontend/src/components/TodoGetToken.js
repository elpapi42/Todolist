import React, { Component } from "react";
import axios from "axios";
import qs from "qs";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

class TodoGetToken extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false
    };
  }

  componentDidMount() {
    let paramscode = new URLSearchParams(location.search);
    const code = paramscode.get("code");
    const url = "http://127.0.0.1:5000/auth/github/";

    const body = {
      auth_code: code,
      auth_state: "123456789asd"
    };

    axios({
      method: "post",
      url: url,
      data: qs.stringify(body),
      headers: {
        "content-type": "application/x-www-form-urlencoded;"
      }
    })
      .then(response => {
        console.log("Details of Response: ", response);
        // console.log("Response Token: " + response.data.token);
        const userSessionData = {
          uToken: response.data.token
        };
        console.log("Saving on sessionStorage(userSessionData): ", userSessionData);
        sessionStorage.setItem("userSess", qs.stringify(userSessionData));
        this.setState({
          isLoggedIn: true
        });
        console.log(this.state.isLoggedIn);
      })
      .catch(error => {
        const token = sessionStorage.getItem("uToken");
        sessionStorage.clear(console.log("sessionStorage Clear"));
        console.log(error);
        this.setState({
          isLoggedIn: false
        });
      });
  }
  render() {
    if (this.state.isLoggedIn === true) {
      return <Redirect to="/App" />;
    } else {
      return (
        <div>
          <h1>Loading</h1>
        </div>
      );
    }
  }
}

export default TodoGetToken;
