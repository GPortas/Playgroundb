import '../../styles/App.css';
import LoginComponent from "./LoginComponent";
import React, {Component} from 'react';
import ContainerComponent from "./ContainerComponent";
import MasterComponent from "../master/MasterComponent";
import StudentComponent from "../student/StudentComponent";
import Cookies from 'universal-cookie';
import {encryptCookieName} from "../../utils/utils";

class InitialComponent extends Component {
    constructor(props) {
        super(props);
        this.setInitialInnerComponent();
    }

    setInitialInnerComponent() {
        const cookies = new Cookies();
        const authCookie = cookies.get(encryptCookieName('authtoken'))
        const userTypeCookie = cookies.get(encryptCookieName('role'))
        if (typeof authCookie == 'undefined') {
            this.state = {nestedComponent: <LoginComponent func={this.onLoginUserInfo.bind(this)}/>};
        } else {
            if (userTypeCookie === "student") {
                this.state = {nestedComponent: <StudentComponent func={this.onUserLogout.bind(this)}/>};
            } else if (userTypeCookie === "master") {
                this.state = {nestedComponent: <MasterComponent func={this.onUserLogout.bind(this)}/>};
            } else {
                this.state = {nestedComponent: <LoginComponent func={this.onLoginUserInfo.bind(this)}/>};
            }
        }
    }

    onUserLogout() {
        const cookies = new Cookies();
        cookies.remove(encryptCookieName('authtoken'));
        cookies.remove(encryptCookieName('role'));
        this.setState({nestedComponent: <LoginComponent func={this.onLoginUserInfo.bind(this)}/>})
    }

    onLoginUserInfo(user) {
        if (user["role"] === "master") {
            this.setState(state => ({
                nestedComponent: <MasterComponent func={this.onUserLogout.bind(this)}/>
            }));
        } else if (user["role"] === "student") {
            this.setState(state => ({
                nestedComponent: <StudentComponent func={this.onUserLogout.bind(this)}/>
            }));
        }
    }

    render() {
        return (
            <ContainerComponent nestedComponent={this.state.nestedComponent}/>
        );
    }
}

export default InitialComponent;