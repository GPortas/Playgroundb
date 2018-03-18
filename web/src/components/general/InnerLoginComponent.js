import '../../styles/App.css';
import $ from 'jquery';
import {Component} from "react";

var React = require('react');

class InnerLoginComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {showInvalidCredentials: false};
    }
    componentDidMount() {
        const self = this;
        $("#logInButton").click(function () {
            $('#logInButton').attr('disabled', true);
            const userEmail = $('#userEmail').val();
            const userPassword = $('#userPassword').val();
            var formData = {
                "email": userEmail,
                "password": userPassword
            }
            $.ajax({
                url: "http://127.0.0.1:8000/login/",
                type: 'post',
                dataType: 'json',
                data: formData,
                success: function (output, status, xhr) {
                    const data = xhr.responseText;
                    const jsonResponse = $.parseJSON(data);
                    self.setState({user: jsonResponse["data"]});
                },
                error: function (jqXHR, exception) {
                    if (jqXHR.status === 401) {
                        self.setState({showInvalidCredentials: true})
                    }
                },
                complete: function () {
                    $('#logInButton').attr('disabled', false);
                }
            });
            $("#signUpButton").click(function () {
                self.setState({user: "newUser"});
            });
        });
    }
    render() {
        if (this.state && this.state.user) {
            this.props.func(this.state.user)
        }
        return (
            <div className="login-div">
                <label className="login-introduction-text">The learning platform that offers teachers and students a
                    cloud environment with all the necessary utilities to manage databases in real time.</label>
                <form>
                    <div className="form-group">
                        <input type="email" className="form-control login-input" id="userEmail"
                               aria-describedby="emailHelp" placeholder="Email"/>
                    </div>
                    <div className="form-group">
                        <input type="password" className="form-control login-input" id="userPassword"
                               placeholder="Password"/>
                        <label id="invalidCredentialsLabel" className="login-invalid-credentials"
                               style={{visibility: this.state.showInvalidCredentials ? 'visible' : 'hidden'}}>Invalid credentials,
                            please try again.</label>
                    </div>
                    <button type="submit" className="btn btn-success common-button" id="logInButton">Log In</button>
                    <button type="submit" className="btn btn-info common-button" id="signUpButton">Sign Up</button>
                </form>
            </div>
        );
    }
}

export default InnerLoginComponent;