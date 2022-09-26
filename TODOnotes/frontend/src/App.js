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
import LoginForm from './components/Auth';
import Cookies from "universal-cookie";
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
    is_auth(){
        return !!this.state.token
    }

    create_user(username, email) {
        const headers = this.get_headers()
        const data = {username:username, email:email}
        axios.post(`http://127.0.0.1:8000/api/users/`, data, {headers}).then(response => {
                this.load_data()
                }
        ).catch(error => {
            console.log(error);
            this.setState({users:[]})});
    }
    delete_user(id) {
        const headers = this.get_headers()
    // state users
        axios.delete(`http://127.0.0.1:8000/api/users/${id}`, {headers}).then(response => {
                console.log(id)
                this.load_data()
                }
        ).catch(error => {
            console.log(error);
            this.setState({users:[]})});
    }

    logout(){
        this.set_token('')
    }
    get_token_from_storage() {
        const coukies = new Cookies()
        const token = coukies.get('token')
        this.setState({'token': token}, ()=> this.load_data())
    }
    set_token(token) {
        const coukies = new Cookies()
        coukies.set('token', token)
        this.senState({'token':token}, () => this.load_data())
        console.log(this.state.token)
    }

    get_token(username, password){
        const data = {username: username, password: password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(
                response => {this.set_token(response.data['token']);}
                ).catch(error =>
                    alert(error+" - неверный логин или пароль"));
    }
    load_data() {
        const headers = this.get_headers()
    // state users
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(
             response => {
                 this.setState(
                 {users: response.data},
                 );}
        ).catch(error => console.log(error));
    // state projects
        axios.get('http://127.0.0.1:8000/api/projects/', headers).then(
             response => {
                 this.setState(
                 {projects: response.data},
                 );}
        ).catch(error => console.log(error));
    // state todoes
            axios.get('http://127.0.0.1:8000/api/todoes/', headers).then(
                response => {
                    this.setState(
                    {todoes: response.data},
                    );}
           ).catch(error => console.log(error));
    }
    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_auth()){
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }
    componentDidMount() {
        this.get_token_from_storage()
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
                    <li>
                        {this.is_auth() ? 
                            <button onClick={() => this.logout()}> 
                            Logout 
                            </button> : 
                            <Link to={this.state.menulinks[4]}>                 {this.state.menuitems[4]}
                            </Link>}
                    </li>
                    </ul>
                </nav>
                    {/* <Route exact path='/' component={<Navigate to='/users' />} /> */}
                <Switch>
                    <Route exact path='/'
                    component={() => <UserList users={this.state.users}/>}
                    component={() => <ProjectList projects={this.state.projects}/>} 
                    component={() => <Todoeslist todoes={this.state.todoes}/>} />
                    
                    <Route exact path='/users' component={() =>     <UserList users={this.state.users}
                    delete_user={(id)=>this.delete_user(id)}/>} 
                    />
                    <Route exact path='/users/create' component={() =>     <UserList users={this.state.users}
                    create_user={(id)=>this.delete_user(id)}/>} 
                    />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} 
                    />                    
                    <Route exact path='/todoes' component={() => <Todoeslist todoes={this.state.todoes}/>} 
                    />
                    <Route exact path='/login'
                        component={()=>
                            <LoginForm
                                get_token={(username, password) =>
                                this.get_token(username, password)}
                            />
                      } 
                    />
                    {/* <Route path='/user/:id'> <UserTodoes todoes={this.state.todoes}/> */}
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
