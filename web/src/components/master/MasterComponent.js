import '../../styles/App.css';
import React, {Component} from 'react';
import ExerciseCreationFormComponent from './ExerciseCreationFormComponent.js'
import ConfigurationComponent from "./ConfigurationComponent";
import ContainerComponent from '../general/ContainerComponent'

import {Navbar, Nav, NavItem} from "react-bootstrap"

class MasterComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {nestedComponent: <ConfigurationComponent/>};
        this.onCommandLineOptionClicked = this.onCommandLineOptionClicked.bind(this);
        this.onExerciseCreationOptionClicked = this.onExerciseCreationOptionClicked.bind(this);
        this.onLeaderboardOptionClicked = this.onLeaderboardOptionClicked.bind(this);
        this.onAccountOptionClicked = this.onAccountOptionClicked.bind(this);
    }

    onCommandLineOptionClicked() {
        this.setState(state => ({
            nestedComponent: <ConfigurationComponent/>
        }));
    }

    onExerciseCreationOptionClicked() {
        this.setState(state => ({
            nestedComponent: <ExerciseCreationFormComponent/>
        }));
    }

    onLeaderboardOptionClicked() {
        //todo: dashboard component
    }

    onAccountOptionClicked() {
        //todo: account component
    }

    render() {
        return (
            <div>
                <Navbar inverse fluid>
                    <Navbar.Header>
                        <Navbar.Brand>
                            <h1 className="App-title" align="left">Playgroun
                                <label style={{color: "#ffa54c"}}>db</label>
                            </h1>
                        </Navbar.Brand>
                    </Navbar.Header>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onCommandLineOptionClicked}>
                            Command Line
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onExerciseCreationOptionClicked}>
                            Exercise Creation
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onLeaderboardOptionClicked}>
                            Leaderboard
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.onAccountOptionClicked}>
                            Account
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" onClick={this.props.func}>
                            Quit
                        </NavItem>
                    </Nav>
                </Navbar>
                <ContainerComponent nestedComponent={this.state.nestedComponent} />
            </div>
        );
    }
}

export default MasterComponent;
