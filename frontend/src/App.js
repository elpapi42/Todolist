import React from "react";
import { Provider } from "react-redux";
import store from "./store";

import Todolist from "./components/Todolist";
import TodoCreateForm from "./components/TodoCreateForm";

function App() {
  return (
    <div className="App">
      <Provider store={store()}>
        <TodoCreateForm />
        <Todolist />
      </Provider>
    </div>
  );
}

export default App;
