import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react'
import { Button } from 'bootstrap';

const CalendarItems = [
  
    {
        "id": 1,
        "name": "Nerdlesque",
        "user": 2,
        "description": "Nerd stuff apply with comments",
        "casting": 1,
        "calendar": 1,
        "is_complete": false
    },
    {
        "id": 2,
        "name": "Zelda",
        "user": 2,
        "description": "Kitten as Tatl... maybe an act?",
        "casting": 2,
        "calendar": 1,
        "is_complete": false
    }
]

class App extends Component{
  constructor(props){
    super(props);
    this.state = {
      viewCompleted: false,
      calItemList: CalendarItems
    };
  }
  displayCompleted = (status)=>{
    if (status){
      return this.setState({ viewCompleted: true });
    }
    return this.setState({viewCompleted: false});
  };
  renderTabList = () =>{
    return(
      <div className="nav nav-tabs">
        <span
          className={this.state.viewCompleted ? "nav-link active": "nav-link"}
          onClick={() => this.displayCompleted(true)}
        >
          Complete
        </span>
        <span
          class={this.state.viewCompleted ? "nav-link":"nav-link active"}
          onClick={()=>this.displayCompleted(false)}
        >
          Incomplete
        </span>
      </div>
    );
  };
  renderItems = () => {
    const {viewCompleted} = this.state;
    const newItems = this.state.calItemList.filter(
      (item) => item.is_complete == viewCompleted
    );
    return newItems.map((item) => (
      <li
        key={item.id}
        className = "list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className = {`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo":""
          }`}
        
          title = {item.description}
          >
            {item.name}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
          >
            Edit
          </button>
          <button
          className="btn btn-danger"
          >
            Delete
          </button>
        </span>  
      </li>
    ));
  };

render() {
  return (
    <main className="container">
      <h1 className="text-white text-uppercase text-center my-4">Your Calendar </h1>
        <div className = "row">
          <div className ="col-md-6 col-sm-10 mx-auto p-0">
            <div className = "card p-3">
              <div className = "mb-4">
                <button
                className = "btn btn-primary"
                >
                  Add Task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
    </main>
  );
}
}
export default App;