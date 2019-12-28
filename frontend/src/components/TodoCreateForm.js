import React, { Component } from "react";
import { connect } from "react-redux";
import { addTodo, newTodo } from "../actions/todos.actions";

class TodoCreateForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: ""
    };
  }

  handleChange = (e) => {
    const { value } = e.target;
    if (value.length <= 30)
      this.setState({
        text: value
      });
    this.props.newTodo(value);
  };

  onClearText = e => {
    this.setState({
      text: ""
    });
  };

  onSaveButton = e => {
    this.props.addTodo(this.state.text);
    e.preventDefault();
  };

  render() {
    return (
      <form>
        <div>
          <input
            type="text"
            value={this.state.text}
            onChange={this.handleChange}
            placeholder="Test"
            required
          />
          <button onClick={this.onSaveButton}>Save</button>
          <button onClick={this.onClearText}>Clear</button>
        </div>
      </form>
    );
  }
}

const mapStateToProps = state => ({});

const mapDispatchToProps = dispatch => ({
  addTodo: text => dispatch(addTodo(text)),
  newTodo: text => dispatch(newTodo(text))
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(TodoCreateForm);
