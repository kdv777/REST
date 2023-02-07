import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import Custom_users_list from './components/custom_users.js';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        'custom_users': []
        }
    }

    componentDidMount() {
//        const custom_users = [
//            {
//                'username':'user1',
//                'firstname':'Ivan',
//                'lastname':'Petrov',
//                'email':'abc@acb.ru'
//            },
//            {
//                'username':'user2',
//                'firstname':'Vasiliy',
//                'lastname':'Terkin',
//                'email':'vasya@terkin.ru'
//            }
//        ]
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
//                const custom_users = response.data
                    this.setState(
                            {
                            'custom_users':response.data
                        }
                    )}).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <Custom_users_list custom_users={this.state.custom_users}/>
            </div>
        )
        }
    }

export default App;
