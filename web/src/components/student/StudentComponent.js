import '../../styles/App.css';
import React, {Component} from 'react';
import MainComponent from '../general/ContainerComponent'
import ExerciseResolutionComponent from './ExerciseResolutionComponent'


import {Navbar, Nav, NavItem} from "react-bootstrap"
import LeaderboardComponent from "../general/LeaderboardComponent";

class StudentComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {nestedComponent: <ExerciseResolutionComponent/>};
        this.onExercisesOptionClicked = this.onExercisesOptionClicked.bind(this);
        this.onLeaderboardOptionClicked = this.onLeaderboardOptionClicked.bind(this);
        this.onAccountOptionClicked = this.onAccountOptionClicked.bind(this);
    }

    onExercisesOptionClicked() {
        this.setState(state => ({
            nestedComponent: <ExerciseResolutionComponent/>
        }));
    }

    onLeaderboardOptionClicked() {
        this.setState(state => ({
            nestedComponent: <LeaderboardComponent/>
        }));
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
                        <NavItem className="navbar-element" onClick={this.onExercisesOptionClicked}>
                            Exercises
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
                <MainComponent nestedComponent={this.state.nestedComponent} />
            </div>
        );
    }
}

export default StudentComponent;
