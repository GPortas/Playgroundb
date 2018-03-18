import '../../styles/App.css';
import {Navbar} from "react-bootstrap"
import githubmark from '../../images/githubmark.png';
import {Component} from "react";
import InnerLoginComponent from "./InnerLoginComponent"
import InnerSignUpComponent from "./InnerSignUpComponent"
import ContainerComponent from "./ContainerComponent"

var React = require('react');

class LoginComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {nestedComponent: <InnerLoginComponent func={this.onUserIdentified.bind(this)}/>};
    }

    onUserIdentified(user) {
        if (user === "newUser"){
            this.setState(state => ({
                nestedComponent: <InnerSignUpComponent/>
            }));
        }
        else {
            this.setState(state => ({
                user: user
            }));
        }
    }

    render() {
        if (this.state && this.state.user) {
            this.props.func(this.state.user)
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
                <ContainerComponent nestedComponent={this.state.nestedComponent}/>
                <div className="login-caption-div">
                    <a href="https://github.com/GPortas/Playgroundb" target="_blank">
                        <img src={githubmark}/>
                    </a>
                    <label className="login-caption-text">GitHub Project</label>
                </div>
            </div>
        );
    }
}

export default LoginComponent;