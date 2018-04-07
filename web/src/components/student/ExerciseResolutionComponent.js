import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils";
import ReactCountdownClock from 'react-countdown-clock'

var React = require('react');

class ExerciseResolutionComponent extends React.Component {
    constructor(props) {
        super(props);
        this.onExerciseNotOvercomed = this.onExerciseNotOvercomed.bind(this);
    }

    componentWillMount() {
        const self = this;
        $.ajax({
            url: "http://127.0.0.1:8000/exercises/",
            dataType: 'json',
            type: 'get',
            headers: generateAuthHeader(),
            crossDomain: true,
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                self.setState({exercises: jsonResponse["data"]});
            },
            complete: function () {
            }
            //todo: Errors treatment!
        });
    }

    componentDidUpdate() {
        const self = this;
        $("#submitButton").click(function () {
            const queryOutput = $('#queryOutput').val();
            var formData = {
                "id": self.state.exercises[0]["_id"],
                "answer": queryOutput,
            }
            $.ajax({
                url: "http://127.0.0.1:8000/validations/",
                dataType: 'json',
                type: 'post',
                headers: generateAuthHeader(),
                data: formData,
                crossDomain: true,
                success: function (output, status, xhr) {
                    const data = xhr.responseText;
                    const jsonResponse = $.parseJSON(data);
                    window.alert(jsonResponse["data"]["is_correct"])
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
            url: "http://127.0.0.1:8000/query-execution/execute-exercise-query/",
            type: 'post',
            dataType: 'json',
            data: formData,
            headers: generateAuthHeader(),
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                const executionResult = jsonResponse["data"]["execution_result"]
                $("#queryOutput").val(executionResult);
            },
            complete: function () {
                $('#executeQueryButton').attr('disabled', false);
            }
            //todo: Errors treatment!
        });
    }

    onExerciseNotOvercomed() {
        //todo
        window.alert("exercise not overcomed");
    }

    render() {
        if (this.state && this.state.exercises) {
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
                                    <ReactCountdownClock seconds={180}
                                                         color="#ffa54c"
                                                         alpha={0.9}
                                                         size={80}
                                                         onComplete={this.onExerciseNotOvercomed}/>
                                    <button className="btn btn-danger exercise-surrender-button"
                                            id="surrenderButton" onClick={this.onExerciseNotOvercomed}>Surrender
                                    </button>
                                </div>
                                <div className="exercise-resolution-stats-inner-div-right">
                                    <label className="common-label">Attempt: 1/3</label>
                                    <br/><br/><br/>
                                    <label className="common-label">Total time: 3 minutes</label>
                                </div>
                            </div>
                        </div>
                        <hr className="exercise-resolution-divider"/>
                        <div className="exercise-resolution-div">
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Query:</label>
                                <CommandLineComponent func={this.onExecute} rows={18}/>
                            </div>
                            <div className="exercise-resolution-inner-div">
                                <label className="exercise-section-title-label">Solution:</label>
                                <textarea readOnly={true} className="form-control query-text-area" id="queryOutput"
                                          rows={18}/>
                                <button type="submit" className="btn btn-success common-button" id="submitButton">Submit
                                    Solution
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            );
        } else {
            // todo: Show loading
            return (
                <div>
                </div>
            )
        }
    }
}

export default ExerciseResolutionComponent;