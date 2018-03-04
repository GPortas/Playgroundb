import '../../styles/App.css';
import LoginComponent from "./LoginComponent";
import React, {Component} from 'react';
import MainComponent from "./MainComponent";
import MasterComponent from "../master/MasterComponent";
import StudentComponent from "../student/StudentComponent";

class InitialComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {nestedComponent: <LoginComponent func={this.changeHandler.bind(this)}/>};
    }

    changeHandler(userType) {
        if(userType === "master"){
            this.setState(state => ({
                nestedComponent: <MasterComponent/>
            }));
        } else if(userType === "student"){
            this.setState(state => ({
                nestedComponent: <StudentComponent/>
            }));
        } else {
            //TODO: show login error
        }
    }

    render() {
        return (
            <MainComponent nestedComponent={this.state.nestedComponent}/>
        );
    }
}

export default InitialComponent;