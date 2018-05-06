import '../../styles/App.css';
import $ from 'jquery';
import {validateEmail, validateNickname, validatePassword} from "../../utils/utils";
import {Component} from "react";

var React = require('react');

class InnerSignUpComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {showInvalidEmail: false};
        this.state = {showInvalidPassword: false};
        this.state = {showInvalidNickname: false};
        this.state = {showUsedCredentials: false};
    }

    componentDidMount() {
        const self = this;
        $("#signUpButton").click(function () {
            const userNickname = $('#userNickname').val()
            const userEmail = $('#userEmail').val();
            const userPassword = $('#userPassword').val();
            self.setState({showUsedCredentials: false});
            let isValidData = true;
            if (validateEmail(userEmail)) {
                self.setState({showInvalidEmail: false});
            } else {
                self.setState({showInvalidEmail: true});
                isValidData = false;
            }

            if (validatePassword(userPassword)) {
                self.setState({showInvalidPassword: false});
            } else {
                self.setState({showInvalidPassword: true});
                isValidData = false;
            }

            if (validateNickname(userNickname)) {
                self.setState({showInvalidNickname: false});
            } else {
                self.setState({showInvalidNickname: true});
                isValidData = false;
            }

            if (isValidData) {
                $('#signUpButton').attr('disabled', true);
                var formData = {
                    "nickname": userNickname,
                    "email": userEmail,
                    "password": userPassword,
                    //Currently only supporting student sign up
                    "role": "student"
                }
                $.ajax({
                    url: process.env.REACT_APP_BASE_URL + "/users/",
                    type: 'post',
                    dataType: 'json',
                    data: formData,
                    success: function (output, status, xhr) {
                        self.props.func()
                    },
                    error: function (jqXHR, exception) {
                        //TODO: handle different errors
                        self.setState({showUsedCredentials: true});
                    },
                    complete: function () {
                        $('#signUpButton').attr('disabled', false);
                    }
                });
            }
        });
    }

    render() {
        return (
            <div className="login-div">
                <label className="login-introduction-text">Welcome to Playgroundb! Please, fill the following form to complete the Sign Up process.</label>
                <form>
                    <div className="form-group">
                        <input type="email" className="form-control sign-up-input" id="userEmail"
                               aria-describedby="emailHelp" placeholder="Email"/>
                        <label id="invalidEmailLabel" className="login-invalid-credentials"
                               style={{visibility: this.state.showInvalidEmail ? 'visible' : 'hidden'}}>Invalid email.
                        </label>
                    </div>
                    <div className="form-group">
                        <input type="password" className="form-control sign-up-input" id="userPassword"
                               placeholder="Password"/>
                        <label id="invalidPasswordLabel" className="login-invalid-credentials"
                               style={{visibility: this.state.showInvalidPassword ? 'visible' : 'hidden'}}>Password must
                            have at least 5 characters.
                        </label>
                    </div>
                    <div className="form-group">
                        <input type="nickname" className="form-control sign-up-input" id="userNickname"
                               placeholder="Nickname"/>
                        <label id="invalidNicknameLabel" className="login-invalid-credentials"
                               style={{visibility: this.state.showInvalidNickname ? 'visible' : 'hidden'}}>Nickname must
                            have at least 3 characters.</label>
                    </div>
                </form>
                <button type="submit" className="btn btn-info common-button" id="cancelButton"
                        onClick={this.props.func}>Go Back
                </button>
                <button type="submit" className="btn btn-info common-button" id="signUpButton">Sign Up</button>
                <label id="usedCredentialsLabel" className="login-invalid-credentials"
                       style={{visibility: this.state.showUsedCredentials ? 'visible' : 'hidden'}}>Email or nickname
                    already used.</label>
            </div>
        );
    }
}

export default InnerSignUpComponent;