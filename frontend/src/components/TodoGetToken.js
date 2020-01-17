import React, { Component } from "react";
import axios from "axios";

class TodoGetToken extends Component {
 constructor(props) {
    super(props);
  }

    componentDidMount() {
    let paramscode = new URLSearchParams(location.search);
    let code = paramscode.get('code');
    let url = 'https://localhost:5000/auth/github/';

  axios.get(url, {code:code})
  .then(function (response) {
    console.log(response);
   })
  .catch((error) => {
    console.log(error);
  });
}
 
   render() {
    return (
      <div>
      	<h1> Authorization Code Received and Sending to Backend </h1>
      </div>
    );
  }
}

export default TodoGetToken;

