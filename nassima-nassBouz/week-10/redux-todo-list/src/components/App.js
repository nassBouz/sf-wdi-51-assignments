import React, { Component } from 'react'
import Todos from './Todos'
import TodoForm from './TodoForm'

class App extends Component {
  render () {
    return (
      <div className="App">
        <h1>Redux TODOS!</h1>
        <TodoForm />
        <Todos />
      </div>
    )
  }
}

export default App
