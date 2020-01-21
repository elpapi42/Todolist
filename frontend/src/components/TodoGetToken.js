import React, { Component } from "react";
import axios from "axios";

class TodoGetToken extends Component {
 constructor(props) {
    super(props);
  }

    componentDidMount() {
    let paramscode = new URLSearchParams(location.search);
    let code = paramscode.get('code');
    let url = "http://127.0.0.1:5000/auth/github/";//{ auth_code:code, auth_state:'123456789asd' 

 let body = {
 	auth_code:code, 
 	auth_state:'123456789asd'
 }
 
  axios({
    method: 'post',
    url: url,
    data: body
  })
  .then((response) => {
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