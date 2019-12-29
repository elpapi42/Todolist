import falseDatabase from "../assets/database/falseDatabase";
// import uuid from "uuidv4";
import {
  TODOS_GET_TODOS,
  TODOS_UPDATE_TODO,
  TODOS_ADD_TODO,
  TODOS_EDIT_NEW_TODO,
  TODOS_DELETE_TODO
} from "./types";

let sid = 3;

export const getTodos = () => dispatch => {
  dispatch({
    type: TODOS_GET_TODOS,
    todos: falseDatabase.todos
  });
};

export const deleteTodo = id => dispatch => {
  dispatch({
    type: TODOS_DELETE_TODO,
    id
  });
};

export const updateTodo = newTodo => dispatch => {
  dispatch({
    type: TODOS_UPDATE_TODO,
    todo: newTodo
  });
};

export const newTodo = name => dispatch => {
  dispatch({
    type: TODOS_EDIT_NEW_TODO,
    name: name
  });
};

export const addTodo = text => dispatch => {
  dispatch({
    type: TODOS_ADD_TODO,
    id: sid++// id: uuid()
  });
};
