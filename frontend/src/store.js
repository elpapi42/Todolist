import { createStore, compose, applyMiddleware } from "redux";
import reducer from "./reducers/main.reducer";
import thunk from "redux-thunk";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const configureStore = () => {
  const store = createStore(
    reducer,
    composeEnhancers(applyMiddleware(thunk)) // thunk required for async action creators
  );

  return store;
};

export default configureStore;
