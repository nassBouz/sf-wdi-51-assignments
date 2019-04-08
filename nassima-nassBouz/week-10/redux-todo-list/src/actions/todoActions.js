import uuid from 'uuid'

export function addTodo (task) {
  return {
    type: 'ADD_TODO',
    todo: {
      id: uuid(),
      task: task,
      completed: false
    }
  }
}

export function toggleTodo (id) {
  return {
    type: 'TOGGLE_TODO',
    // same as id:id
    id
  }
}

export function UpdateTodo(id, task){
    let todo = this.props.todo
    return {
        type: ' UPDATE_TODO',
        todo: {
          task: task,
        }
    }
}

