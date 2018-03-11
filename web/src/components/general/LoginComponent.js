import '../../styles/App.css';
import $ from 'jquery';
import {Navbar} from "react-bootstrap"
import githubmark from '../../images/githubmark.png';

var React = require('react');
var createReactClass = require('create-react-class');

const LoginComponent = createReactClass({
    componentDidMount() {
        const self = this;
        $("#loginButton").click(function () {
            const userEmail = $('#userEmail').val();
            const userPassword = $('#userPassword').val();
            //TODO: AJAX CALL TO AUTHENTICATION
            //user types: unknown, student, master
            //Just for test purpose:
            if(userEmail === 'a@a.com') {
                self.setState({userType: "master"});
            } else {
                self.setState({userType: "student"});
            }
        });
    },
    render() {
        if (this.state && this.state.userType) {
            this.props.func(this.state.userType)
        }
        return (
            <div className="login-background">
                <Navbar inverse>
                    <Navbar.Header>
                        <Navbar.Brand>
                            <h1 className="App-title" align="left">Playgroun
                                <label style={{color: "#ffa54c"}}>db</label>
                            </h1>
                        </Navbar.Brand>
                    </Navbar.Header>
                </Navbar>
                <div className="login-div">
                    <form>
                        <div className="form-group">
                            <input type="email" className="form-control login-input" id="userEmail"
                                   aria-describedby="emailHelp" placeholder="Email"/>
                        </div>
                        <div className="form-group">
                            <input type="password" className="form-control login-input" id="userPassword"
                                   placeholder="Password"/>
                        </div>
                        <button type="submit" className="btn btn-success common-button" id="loginButton">Sign In</button>
                        <button type="submit" className="btn btn-info common-button" id="loginButton">Sign Up</button>
                    </form>
                    <h1 className="login-introduction-text">Playgroundb is the learning platform that offers teachers and students a cloud environment with all the necessary utilities to manage databases in real time.</h1>
                </div>
                <div className="login-caption-div">
                    <a href="https://github.com/GPortas/Playgroundb" target="_blank">
                        <img  src={githubmark}/>
                    </a>
                    <label className="login-caption-text">GitHub Project</label>
                </div>
            </div>
        );
    }
});

export default LoginComponent;