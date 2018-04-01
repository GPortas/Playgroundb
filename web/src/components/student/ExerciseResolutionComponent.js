import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils";

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseResolutionComponent = createReactClass({
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
    },

    componentDidUpdate() {
        const self = this;
        $("#submitButton").click(function(){
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
    },

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
            success: function(output, status, xhr) {
                const data=xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                const executionResult = jsonResponse["data"]["execution_result"]
                $("#queryOutput").val(executionResult);
            },
            complete: function () {
                $('#executeQueryButton').attr('disabled', false);
            }
            //todo: Errors treatment!
        });
    },

    render() {
        if (this.state && this.state.exercises) {
            return (
                <div>
                    <div className="common-div">
                        <label className="common-label">Statement:</label>
                        <hr className="exercise-resolution-divider"/>
                        <label className="common-label">
                            {this.state.exercises[0]["question"]}
                        </label>
                    </div>
                    <div className="common-div">
                        <div className="exercise-resolution-div">
                            <div className="exercise-resolution-inner-div">
                                <label className="common-label">Query:</label>
                                <div className="exercise-resolution-left-bottom-div">
                                    <CommandLineComponent func={this.onExecute} rows={18}/>
                                </div>
                            </div>
                            <div className="exercise-resolution-inner-div">
                                <label className="common-label">Solution:</label>
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
});

export default ExerciseResolutionComponent;