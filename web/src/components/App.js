import React, {Component} from 'react';
import ExerciseCreationFormComponent from './exercise/ExerciseCreationComponent.js'
import '../styles/App.css';

class App extends Component {
    render() {
        return (
            <div className="App">
                <header className="App-header">
                    <h1 className="App-title" align="left">Playgroun
                        <label style={{color: "#ffa54c"}}>db</label>
                    </h1>
                </header>
                <ExerciseCreationFormComponent/>
            </div>
        );
    }
}

export default App;
