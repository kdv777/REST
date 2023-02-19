import React from 'react';
import axios from 'axios';
//import logo from './logo.svg';
import './App.css';
//import Custom_users_list from './components/custom_users.js';
//import Footer from './components/Footer.js';
//import Menu from './components/Menu.js';
import UserList from './components/User.js';
import ProjectList from './components/Project.js';
import ToDoList from './components/ToDo.js';
import {BrowserRouter, Route, Link, Switch} from 'react-router-dom'

const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {

    constructor(props) {
        super(props);
        const user1 = {id: 1, first_name: 'User1', last_name: 'UserLastName1', email: 'user1@mail.ru', project: '1'}
        const users = [user1]
        const project1 = {id: 1, name: 'Project1', repo_link: 'http://repo1.ru'}
        const projects = [project1]
        const todo1 = {id: 1, title: 'Title1', body: 'Lorem1', author: '1'}
        const todos = [todo1]

        this.state = {
        'users': users,
        'projects': projects,
        'todos': todos
        }
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/user_set/')
            .then(response => {

                    this.setState({users: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/Project/')
            .then(response => {

                    this.setState({projects: response.data})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/TODO/')
            .then(response => {

                    this.setState({todos: response.data})
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                <nav>
                    <ul>
                        <li>
                           <Link to='/'>Users</Link>
                        </li>
                        <li>
                           <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                           <Link to='/TODO'>ToDos</Link>
                        </li>
                    </ul>
                </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList
                        users={this.state.users} />} />
                        <Route exact path='/projects' component={() => <ProjectList
                        projects={this.state.projects} />} />
                        <Route exact path='/TODO' component={() => <ToDoList
                        projects={this.state.todos} />} />
                        <Route component={NotFound404} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
        }
    }

export default App;
