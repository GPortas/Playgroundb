import '../../styles/App.css';
import $ from 'jquery';

var React = require('react');
var createReactClass = require('create-react-class');

const InnerSignUpComponent = createReactClass({
    componentDidMount() {
    },
    render() {
        if (this.state && this.state.userType) {
            this.props.func(this.state.userType)
        }
        return (
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
                    <div className="form-group">
                        <input type="nickname" className="form-control login-input" id="userNickname"
                               placeholder="Nickname"/>
                    </div>
                    <button type="submit" className="btn btn-info common-button" id="signUpButton">Sign Up</button>
                </form>
            </div>
        );
    }
});

export default InnerSignUpComponent;