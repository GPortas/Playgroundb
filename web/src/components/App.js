import React, {Component} from 'react';
import ExerciseCreationFormComponent from './exercise/ExerciseCreationComponent.js'
import '../styles/App.css';

import {Navbar, Nav, NavItem} from "react-bootstrap"

class App extends Component {
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
                        <NavItem className="navbar-element" eventKey={1} href="#">
                            Command Line
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" eventKey={1} href="#">
                            Exercise Creation
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" eventKey={1} href="#">
                            Dashboard
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" eventKey={1} href="#">
                            Account
                        </NavItem>
                    </Nav>
                    <Nav>
                        <NavItem className="navbar-element" eventKey={1} href="#">
                            Quit
                        </NavItem>
                    </Nav>
                </Navbar>
                <div className="App">
                    <ExerciseCreationFormComponent/>
                </div>
            </div>
        );
    }
}

export default App;
