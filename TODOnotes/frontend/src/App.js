import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import UserList from './components/user.js';
import Menu from './components/Menu.js';
import MenuLinks from './components/Menu.js';
import Footer from './components/Footer.js';
import ProjectList from './components/projects.js';
import Todoeslist from './components/todoes.js';
import NotFound404 from './components/Notfound404.js';
import UserTodoes from './components/details.js';
import LoginForm from './components/Auth.js';

// import {HashRouter, Route} from 'react-router-dom';
import {BrowserRouter, Route,  Link,  useLocation, Switch, Redirect} from 'react-router-dom'

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
            token: '',
            menuitems: ["Главная", "Авторы", "Проекты", "Заметки", "Login"],
            menulinks:  ["/", "/users", "/projects", "/todoes", "/login"],
            footer: ["О нас"],
            footer_links: ["/"],
        }
    }
    get_token(username, password){
        console.log(username, password)
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
                {/* <Menu menuitems={this.state.menuitems}/> */}
                {/* <MenuLinks menulinks={this.state.menulinks}/> */}
            </header>
            <main>
            <div>
                {/* <UserList users={this.state.users}/> */}
                {/* <ProjectList projects={this.state.projects}/> */}
                <BrowserRouter>
                {/* <Routes> */}
                <nav>
                    <ul>
                    <li><Link to={this.state.menulinks[0]}>{this.state.menuitems[0]}</Link></li>
                    <li><Link to={this.state.menulinks[1]}>{this.state.menuitems[1]}</Link></li>
                    <li><Link to={this.state.menulinks[2]}>{this.state.menuitems[2]}</Link></li>
                    <li><Link to={this.state.menulinks[3]}>{this.state.menuitems[3]}</Link></li>
                    <li><Link to={this.state.menulinks[4]}>{this.state.menuitems[4]}</Link></li>
                    </ul>
                </nav>
                    {/* <Route exact path='/' component={<Navigate to='/users' />} /> */}
                <Switch>
                    <Route exact path='/'
                    component={() => <UserList users={this.state.users}/>}
                    component={() => <ProjectList projects={this.state.projects}/>} 
                    component={() => <Todoeslist todoes={this.state.todoes}/>} />
                    
                    <Route exact path='/users' component={() => <UserList users={this.state.users}/>} />   
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} />                    
                    <Route exact path='/todoes' component={() => <Todoeslist todoes={this.state.todoes}/>} />
                    <Route exact path='/login'
                        component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)}/>} />
                    <Route path='/user/:id'> <UserTodoes todoes={this.state.todoes}/>

                    </Route>
                    <Redirect from='user' to='users' />
                    <Route component={NotFound404} />
                    
                </Switch>
                {/* </Routes> */}
                </BrowserRouter>
            </div>
            </main>
            <Footer footer={this.state.footer}/>
        </div>
            )}}
export default App;
