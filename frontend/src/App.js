import React from "react";
import { Provider } from "react-redux";
import store from "./store";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";

import Todolist from "./components/Todolist";
import TodoCreateForm from "./components/TodoCreateForm";
import LoginGithub from "./components/LoginGithub";
import TodoGetToken from "./components/TodoGetToken";

function App() {
  return (
    <div className="App">
      <Provider store={store()}>
        <Router>
          <Switch>
            <Route exact path="/">
              <h2>Login</h2>
              <LoginGithub />
            </Route>
            <Route path="/App">
              <TodoCreateForm />
              <Todolist />
            </Route>
            <Route path="/login/github/authorized/">
              <TodoGetToken />
            </Route>
            <Route>
              <h1> 404 Not Found</h1>
            </Route>
          </Switch>
        </Router>
      </Provider>
    </div>
  );
}

export default App;
