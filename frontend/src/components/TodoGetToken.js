import React, { Component } from "react";
import axios from "axios";

class TodoGetToken extends Component {
 constructor(props) {
    super(props);
  }

    componentDidMount() {
    	let params = new URLSearchParams(location.search);
      let code = params.get('code');
    }
// let url = "https://pokeapi.co/api/v2/pokemon/1/"; Peticion al servidor pidiendo el token
// axios.get(url)
//   .then(function (response) {
//     // handle success
//     console.log(response);
//   })
//   .catch(function (error) {
//     // handle error
//     console.log(error);
//   })
//   .finally(function () {
//     // always executed
//   });
// }

   render() {
    return (
      <div>
      	<h1> Authorization Code Received and Sending to Backend </h1>
      </div>
    );
  }
}

export default TodoGetToken;

