import React, { Component } from "react";
import { connect } from "react-redux";
import { deleteTodo } from "../actions/todos.actions";
import { updateTodo } from "../actions/todos.actions";

class Todo extends Component {
  render() {
    const { todo } = this.props;
    const onChange = () => {
      const newTodo = { ...this.props.todo };

      newTodo.finished = !newTodo.finished;

      this.props.updateTodo(newTodo);
    };
    return (
      <div>
        <span>
          <input type="checkbox" onChange={onChange} checked={todo.finished}></input>
          {todo.name}
          <button
            onClick={() => {
              this.props.deleteTodo(this.props.id);
            }}
          >
            Delete
          </button>
        </span>
      </div>
    );
  }
}

const mapStateToProps = () => ({});

const mapDispatchToProps = dispatch => ({
  updateTodo: newTodo => dispatch(updateTodo(newTodo)),
  deleteTodo: id => dispatch(deleteTodo(id))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Todo);
