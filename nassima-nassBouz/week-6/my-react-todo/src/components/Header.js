import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Header extends Component{
  render(){
    return (
      <header>
        <h1>ToDo</h1>
        <nav> 
         <li><Link to={'/'}>Home</Link></li> 
         <li> <Link to={'/todos'}>Todos</Link></li> 
        </nav>
      </header>
    )
  }
}

export default Header