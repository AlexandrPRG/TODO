import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from './components/user.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';

const DOMAIN = 'http://127.0.0.1:8000/api/';
// const get_url = (url) =>  `${DOMAIN}${URL}`;
// console.log("get_url=")

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            users: [],
//          projects: [],
//          todoes: [],
            menuitems: ["Главная", "Авторы", "Заметки"],
            menulinks:  ["/", "/users", "/todoes"],
            footer: ["О нас"],
        }
    }
    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(
        //    state => console.log(get_url('users/'))
             response => {
                 this.setState(
                 {users: response.data},
                 );}
        ).catch(error => console.log(error));
    }
    render () {
        return (
        <div>
            <header>
                <Menu menuitems={this.state.menuitems}/>
            </header>
            <main>
                {/* <Menu menulinks={this.state.menulinks}/> */}
                <UserList users={this.state.users}/>
            </main>
            <Footer footer={this.state.footer}/>
        </div>
            )}}
export default App;
