import React, { Component } from 'react'
import { connect } from 'react-redux'
import { addTodo } from '../actions/todoActions'

class TodoForm extends Component {
  state = {
    newTodo: ''
  }

  handleChange = (event) => {
    console.log(event.target.value)
    this.setState({ newTodo: event.target.value })
  }

  handleSubmit = (event) => {
    event.preventDefault()
    this.props.addTodo(this.state.newTodo)
    this.setState({ newTodo: '' })
  }

  render () {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          onChange={this.handleChange}
          value={this.state.newTodo}
        />
        <button>Add Todo</button>
      </form>
    )
  }

}

export default connect(null, { addTodo })(TodoForm)