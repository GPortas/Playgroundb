import '../../styles/App.css';
import $ from 'jquery';
import {Navbar} from "react-bootstrap"

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
            <div>
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
                        <button type="submit" className="btn btn-success common-button" id="loginButton">Log In</button>
                    </form>
                </div>
            </div>
        );
    }
});

export default LoginComponent;