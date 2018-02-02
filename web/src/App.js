import React, {Component} from 'react';
import ExerciseCreationFormComponent from './ExerciseCreationComponent.js'
import './App.css';

class App extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title" align="left">Playgroun
                        <text style={{color: "#ffa54c"}}>db</text>
                    </h1>
                </header>
                <ExerciseCreationFormComponent/>
            </div>
        );
    }
}

export default App;
