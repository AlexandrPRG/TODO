import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from './components/user.js';
import Menu from './components/Menu.js';
import Footer from './components/Footer.js';
import ProjectList from './components/projects.js';
import Todoeslist from './components/todoes.js';

// import {HashRouter, Route} from 'react-router-dom';
import {BrowserRouter, Route,  Link,  useLocation} from 'react-router-dom'

const DOMAIN = 'http://127.0.0.1:8000/api/';
// const get_url = (url) =>  `${DOMAIN}${URL}`;
// console.log("get_url=")

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            users: [],
            projects: [],
            todoes: [],
            menuitems: ["Главная", "Авторы", "Проекты", "Заметки"],
            menulinks:  ["/", "/users", "/todoes", "/projects"],
            footer: ["О нас"],
            footer_links: ["/"],
        }
    }

    componentDidMount() {
    // state users
        axios.get('http://127.0.0.1:8000/api/users/').then(
        //    state => console.log(get_url('users/'))
             response => {
                 this.setState(
                 {users: response.data},
                 );}
        ).catch(error => console.log(error));
    // state projects
        axios.get('http://127.0.0.1:8000/api/projects/').then(
             response => {
                 this.setState(
                 {projects: response.data},
                 );}
        ).catch(error => console.log(error));
    // state todoes
            axios.get('http://127.0.0.1:8000/api/todoes/').then(
                response => {
                    this.setState(
                    {todoes: response.data},
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
            <div>
                {/* <UserList users={this.state.users}/> */}
                {/* <ProjectList projects={this.state.projects}/> */}
                <BrowserRouter>
                {/* <Routes> */}
                    {/* <Route exact path='/' component={<Navigate to='/users' />} /> */}
                    <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} />                    
                    <Route exact path='/todoes' component={() => <Todoeslist todoes={this.state.todoes}/>} />
                {/* </Routes> */}
                </BrowserRouter>
            </div>
            </main>
            <Footer footer={this.state.footer}/>
        </div>
            )}}
export default App;
