import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from './components/user.js'

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': []
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
            response =>{
                this.setState({
                    state:{
                        'users': response.data
        }});}).catch(error => console.log(error))
//        const users = [
//            {
//            'first_name': 'fn1',
//            'last_name': 'ln1',
//            'email': 'email1@em.com'
//            },
//            {
//            'first_name': 'fn2',
//            'last_name': 'ln2',
//            'email': 'email2@em.com'
//            },
//        ]
    }
    render () {
        return (
            <div>
                <UserList users={this.state.users}/>
            </div>
            )}}
export default App;
