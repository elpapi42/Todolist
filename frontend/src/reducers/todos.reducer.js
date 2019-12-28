import {
  TODOS_GET_TODOS,
  TODOS_UPDATE_TODO,
  TODOS_ADD_TODO,
  TODOS_EDIT_NEW_TODO,
  TODOS_DELETE_TODO
} from "../actions/types";

const initialState = {
  todos: [],
  newTodo: {
    name: ""
  }
};
export default (state = initialState, action) => {
  switch (action.type) {
    case TODOS_GET_TODOS: {
      const { todos } = action;

      return { ...state, todos };
    }
    case TODOS_DELETE_TODO: {
      const { id } = action;
      const todos = state.todos.filter(todo => id !== todo.id);
      return { ...state, todos };
    }
    case TODOS_UPDATE_TODO: {
      const newtodo = action.todo;
      const newArrayTodos = [...state.todos];
      const indexNewTodo = newArrayTodos.findIndex(todo => todo.id === newtodo.id);
      if (indexNewTodo === -1) return { ...state };

      newArrayTodos[indexNewTodo] = { ...newArrayTodos[indexNewTodo], ...newtodo };
      console.log(newArrayTodos);
      return {
        ...state,
        todos: newArrayTodos
      };
    }
    case TODOS_ADD_TODO: {
      const newT = {
        todos: [
          ...state.todos,
          {
            id: action.id,
            name: state.newTodo.name,
            finished: false
          }
        ]
      };

      localStorage.setItem("todos", JSON.stringify(newT.todos));
      const save = localStorage.getItem("todos");
      console.log("Objeto: ", JSON.parse(save));

      return Object.assign({}, state, newT);
    }
    case TODOS_EDIT_NEW_TODO: {
      state.newTodo = {
        name: action.name
      };
      return { ...state };
    }
    default: {
      return state;
    }
  }
};
