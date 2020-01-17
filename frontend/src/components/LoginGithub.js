import React from "react";
import axios from "axios";

function LoginGithub() {

let url = new URL('https://github.com/login/oauth/authorize/');
let params = [ ['client_id','8ee5e9f88fea3247194c'] , ['scope','user:email'] ];
// let params = {client_id:8ee5e9f88fea3247194c, scope: user:email};
url.search = new URLSearchParams(params).toString();

  return (
    <div>
    <a href={url}>Log In with Github</a>
    </div>
  );
}

export default LoginGithub;