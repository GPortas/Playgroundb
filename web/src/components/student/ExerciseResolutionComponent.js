import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils"
import ReactCountdownClock from 'react-countdown-clock'
import statusscreenshot from '../../images/statusscreenshot.png';
import mathexpression from '../../images/mathexpression.png';

var React = require('react');

class ExerciseResolutionComponent extends React.Component {
    constructor(props) {
        super(props);
        this.loadNextExercise = this.loadNextExercise.bind(this);
        this.onExecute = this.onExecute.bind(this);
        this.loadExercises = this.loadExercises.bind(this);
        this.setState({noExercisesAvailable: false, shouldShowWrongSolutionLabel: false});
    }

    loadExercises() {
        const self = this;
        $('#loadButton').attr('disabled', true);
        $.ajax({
            url: process.env.REACT_APP_BASE_URL + "/exercises/",
            dataType: 'json',
            type: 'get',
            headers: generateAuthHeader(),
            crossDomain: true,
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                self.setState({exercises: jsonResponse["data"]});
                if (!self.state.exercises[0]) {
                    self.setState({noExercisesAvailable: true});
                }
            },
            complete: function () {
                $('#loadButton').attr('disabled', false);
            }
            //todo: Errors treatment!
        });
    }

    componentDidUpdate() {
        const self = this;
        $("#submitButton").unbind("click").click(function () {
            $('#submitButton').attr('disabled', true);
            const timeLeft = self.refs.timer._seconds;
            const queryOutput = $('#queryOutput').val();
            var formData = {
                "exercise_id": self.state.exercises[0]["_id"],
                "answer": queryOutput,
                "time_left": timeLeft,
            }
            $.ajax({
                url: process.env.REACT_APP_BASE_URL + "/validations/",
                dataType: 'json',
                type: 'post',
                headers: generateAuthHeader(),
                data: formData,
                crossDomain: true,
                success: function (output, status, xhr) {
                    const data = xhr.responseText;
                    const jsonResponse = $.parseJSON(data);
                    if (jsonResponse["data"]["is_correct"]) {
                        self.setState({shouldShowWrongSolutionLabel: false});
                        self.loadNextExercise()
                    }
                    else {
                        self.setState({shouldShowWrongSolutionLabel: true});
                    }
                },
                complete: function () {
                    $('#submitButton').attr('disabled', false);
                }
                //todo: Errors treatment!
            });
        });
    }

    onExecute(inputQuery) {
        const self = this;
        $('#executeQueryButton').attr('disabled', true);
        var formData = {
            "query": inputQuery,
            "exercise_id": self.state.exercises[0]["_id"]
        }
        $.ajax({
            url: process.env.REACT_APP_BASE_URL +"/query-execution/execute-exercise-query/",
            type: 'post',
            dataType: 'json',
            data: formData,
            headers: generateAuthHeader(),
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                const executionResult = jsonResponse["data"]["execution_result"];
                $("#queryOutput").val(executionResult);
            },
            complete: function () {
                $('#executeQueryButton').attr('disabled', false);
            }
            //todo: Errors treatment!
        });
    }

    loadNextExercise() {
        this.clearTextAreas();
        let exercises = this.state.exercises;
        exercises.shift();
        this.setState({exercises: exercises, shouldShowWrongSolutionLabel: false});
    }

    clearTextAreas() {
        this.refs.child.clearInputQueryTextArea();
        $("#queryOutput").val("");
    }

    render() {
        if (this.state && this.state.exercises[0]) {
            return (
                <div>
                    <div className="common-div">
                        <div className="exercise-resolution-div">
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Statement:</label>
                                <hr className="exercise-resolution-divider"/>
                                <label className="common-label">
                                    {this.state.exercises[0]["question"]}
                                </label>
                                <br/><br/><br/>
                                <label className="common-label">Collection
                                    name: {this.state.exercises[0]["collection_name"]}</label>
                            </div>
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Status:</label>
                                <hr className="exercise-resolution-divider"/>
                                <div className="exercise-resolution-stats-inner-div-left">
                                    <ReactCountdownClock ref="timer"
                                                         seconds={this.state.exercises[0]["time"] + 0.0000001}
                                                         color="#ffa54c"
                                                         alpha={0.9}
                                                         size={80}
                                                         onComplete={this.loadNextExercise}/>
                                </div>
                                <div className="exercise-resolution-stats-inner-div-right">
                                    <button className="btn btn-danger exercise-surrender-button"
                                            id="surrenderButton" onClick={this.loadNextExercise}>Surrender
                                    </button>
                                    <div id="wrongSolutionLabel" style={{visibility: this.state.shouldShowWrongSolutionLabel ? 'visible' : 'hidden'}}>
                                        <label className="exercise-wrong-solution-label">Wrong solution... Try again!</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr className="exercise-resolution-divider"/>
                        <div className="exercise-resolution-div">
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Query:</label>
                                <CommandLineComponent func={this.onExecute} rows={18} ref="child"/>
                            </div>
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Solution:</label>
                                <textarea readOnly={true} className="form-control query-text-area" id="queryOutput"
                                          rows={18}/>
                                <button type="submit" className="btn btn-success common-button"
                                        id="submitButton">Submit
                                    Solution
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            );
        } else {
            if (this.state && this.state.noExercisesAvailable) {
                return (
                    <div className="common-div">
                        <div>
                            <label className="exercise-section-title-label">Exercises section</label>
                        </div>
                        <br/><br/><br/>
                        <label className="common-label">We do not have new exercises for you :(<br/><br/>But you can come back later to check if new ones have been uploaded :)</label>
                    </div>
                )
            } else {
                return (
                    <div className="common-div">
                        <div>
                            <label className="exercise-section-title-label">Exercises section</label>
                        </div>
                        <br/><br/><br/>
                        <div>
                            <label className="common-label">In this section, you will find a collection of exercises to solve. Each exercise has a maximum time to be solved.</label>
                        </div>
                        <br/><br/>
                        <br/><br/>
                        <div>
                            <label className="common-label">For each exercise you have the surrender option by pressing the red surrender button.</label>
                        </div>
                        <br/><br/>
                        <br/><br/>
                        <div>
                            <img src={statusscreenshot}/>
                        </div>
                        <br/><br/>
                        <div>
                            <label className="common-label">The score for each solved exercise will be obtained from the following expression:</label>
                        </div>
                        <div>
                            <img src={mathexpression}/>
                        </div>
                        <br/><br/>
                        <div>
                            <label className="common-label">If you surrender or time ends, the exercise will appear in future executions until it is solved, increasing the total number of attempts in each occurrence.</label>
                        </div>
                        <br/><br/>
                        <br/><br/>
                        <br/><br/>
                        <div>
                            <button id="loadButton" type="submit" className="btn btn-success ready-button" onClick={this.loadExercises}>Load Exercises</button>
                        </div>
                        <br/><br/>
                    </div>
                )
            }
        }
    }
}

export default ExerciseResolutionComponent;