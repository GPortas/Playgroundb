import '../../styles/App.css';
import React, {Component} from 'react';
import MainComponent from '../general/ContainerComponent'
import ExerciseResolutionComponent from './ExerciseResolutionComponent'


import {Navbar, Nav, NavItem} from "react-bootstrap"

class StudentComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {nestedComponent: <ExerciseResolutionComponent/>};
        this.onExercisesOptionClicked = this.onExercisesOptionClicked.bind(this);
        this.onQuitOptionClicked = this.onQuitOptionClicked.bind(this);
        this.onDashboardOptionClicked = this.onDashboardOptionClicked.bind(this);
        this.onAccountOptionClicked = this.onAccountOptionClicked.bind(this);
    }

    onExercisesOptionClicked() {
        this.setState(state => ({
            nestedComponent: <ExerciseResolutionComponent/>
        }));
    }

    onDashboardOptionClicked() {
        //todo: dashboard component
    }

    onAccountOptionClicked() {
        //todo: account component
    }

    onQuitOptionClicked() {
        //todo: logout user
    }

    render() {
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
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onExercisesOptionClicked}>
                            Exercises
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onDashboardOptionClicked}>
                            Dashboard
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onAccountOptionClicked}>
                            Account
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onQuitOptionClicked}>
                            Quit
                        </NavItem>
                    </Nav>
                </Navbar>
                <MainComponent nestedComponent={this.state.nestedComponent} />
            </div>
        );
    }
}

export default StudentComponent;
