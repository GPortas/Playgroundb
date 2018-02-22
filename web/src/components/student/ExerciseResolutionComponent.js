import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseResolutionComponent = createReactClass({
    changeHandler(solutionText) {
        $("#queryOutput").val(solutionText);
    },

    render() {
        return (
            <div>
                <div className="common-div">
                    <div className="exercise-resolution-left-div">
                        <label className="common-label">Statement:</label>
                        <hr className="exercise-resolution-divider"/>
                        <label className="common-label">
                            Here goes an exercise statement
                        </label>
                        <div className="exercise-resolution-left-bottom-div">
                            <CommandLineComponent func={this.changeHandler} rows={6}/>
                        </div>
                    </div>
                    <div className="exercise-resolution-right-div">
                        <label className="common-label">Solution:</label>
                        <textarea readOnly={true} className="form-control query-text-area" id="queryOutput" rows={18}/>
                        <button type="submit" className="btn btn-success common-button" id="submitButton">Submit Solution</button>
                    </div>
                </div>
            </div>
        );
    }
});

export default ExerciseResolutionComponent;