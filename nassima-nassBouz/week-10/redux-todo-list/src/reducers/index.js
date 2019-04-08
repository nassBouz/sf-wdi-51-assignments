import { combineReducers } from 'redux'
import todos from './todoReducer'

// Combine all our reducers together
const rootReducer = combineReducers({
  todos
})

export default rootReducer