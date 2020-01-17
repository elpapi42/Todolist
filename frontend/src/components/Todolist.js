import React, { Component } from "react";
import { connect } from "react-redux";
import { getTodos } from "../actions/todos.actions";
import Todo from "./Todo";

class Todolist extends Component {
  componentDidMount() {
    this.props.getTodos();
  }

  render() {
    const { todos } = this.props;
    return (
      <div>
        <h2>Tasks</h2>
        <div>
          {todos.map(todo => (
            <Todo todo={todo} key={todo.id} id={todo.id} />
          ))}
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  todos: state.todos.todos
});

const mapDispatchToProps = dispatch => ({
  getTodos: () => dispatch(getTodos())
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Todolist);
