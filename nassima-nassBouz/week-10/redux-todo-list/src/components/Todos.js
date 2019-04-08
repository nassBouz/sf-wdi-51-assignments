import React, { Component } from 'react'
import { connect } from 'react-redux'
import { toggleTodo } from '../actions/todoActions'
import {UpdateTodo} from '../actions/todoActions'
import { bindActionCreators } from 'redux';

class Todos extends Component {
  render () {
    return (
      <div>
        <ul>
          {this.props.todos.map(todo => (
           <li
             key={todo.id}
             onClick={() => this.props.toggleTodo(todo.id)} //Why do we wrap this in an arrow function?
             >
             {todo.task}: {todo.completed.toString()}
           </li>
          ))}
          {this.props.todos.map(todo => (
           <li
             key={todo.id}
             onClick={() => this.props.UpdateTodo(todo.id)}//Why do we wrap this in an arrow function?
             >
             EDIT 
           </li>
          ))}
        </ul>
      </div>
    )
  }
}

const mapStateToProps = (state) => {
  return {
    todos: state.todos
  }
}

export default connect(mapStateToProps, { toggleTodo , UpdateTodo})(Todos)