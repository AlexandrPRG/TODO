import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from './components/user.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            users: [],
//            projects: [],
//            todos: [],
            menuitem: ["Главная", "Авторы", "Заметки"],
            footer: ["О нас"],
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
            response => {
                this.setState(
                {users: response.data},
                );}
        ).catch(error => console.log(error));
    }
    render () {
        return (
        <div>
            <Menu menuitem={this.state.menuitem}/>
            <UserList users={this.state.users}/>
            <Footer footer={this.state.footer}/>
        </div>
            )}}
export default App;
