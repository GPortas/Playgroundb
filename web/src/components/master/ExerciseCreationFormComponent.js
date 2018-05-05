import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils";

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseCreationFormComponent = createReactClass({
    onExecute(inputText) {
        $('#executeQueryButton').attr('disabled', true);
        var formData = {
            "query": inputText,
        }
        $.ajax({
            url: process.env.REACT_APP_BASE_URL + "/query-execution/",
            type: 'post',
            dataType: 'json',
            data: formData,
            headers: generateAuthHeader(),
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                const executionResult = jsonResponse["data"]["execution_result"]
                $("#inputSolution").val(executionResult);
            },
            complete: function () {
                $('#executeQueryButton').attr('disabled', false);
            }
            //todo: Errors treatment!
        });
    },

    componentDidMount() {
        $("#submitButton").click(function () {
            $('#submitButton').attr('disabled', true);
            const exerciseStatement = $('#inputStatement').val();
            const exerciseSolution = $('#inputSolution').val();
            const exerciseCollectionName = $('#inputCollectionName').val();
            const exerciseTime = $('#inputTime').val();
            var formData = {
                "author": "testauthor",
                "question": exerciseStatement,
                "solution": exerciseSolution,
                "collection_name": exerciseCollectionName,
                "time": exerciseTime
            }
            $.ajax({
                url: process.env.REACT_APP_BASE_URL + "/exercises/",
                dataType: 'json',
                type: 'post',
                headers: generateAuthHeader(),
                data: formData,
                crossDomain: true,
                complete: function () {
                    $('#submitButton').attr('disabled', false);
                }
                //todo: Errors treatment!
            });
        });
    },
    render() {
        return (
            <div className="common-div App">
                <form>
                    <div className="form-group">
                        <label htmlFor="inputStatement" className="common-label">Write the statement of the
                            exercise:</label>
                        <textarea className="form-control input-text" id="inputStatement"
                                  aria-describedby="statement" rows="6"/>
                        <label id="statementHelp" className="form-text text-muted">Try to be as concise as possible
                            because this will be the statement that your students will receive.
                        </label>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputCollectionName" className="common-label">Type the name of the collection
                            that contains the data source:</label>
                        <textarea className="form-control input-text" id="inputCollectionName"
                                  aria-describedby="statement" rows="1" style={{resize: 'none'}}/>
                        <label id="inputCollectionHelp" className="form-text text-muted">
                            Check that the name is correct to prevent errors.
                        </label>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputTime" className="common-label">Set the maximum time to solve the exercise
                            (seconds):</label>
                        <input type="number" min="0" id="inputTime" className="common-label"
                               aria-describedby="statement" style={{resize: 'none', width: '100%', fontSize: 'medium'}}/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputSolution" className="common-label">Write the expected result
                            after executing the necessary query:</label>
                        <textarea className="form-control input-text" id="inputSolution" rows="6"
                                  placeholder={"{\"data\": {}}"}/>
                        <label id="solutionHelp" className="form-text text-muted">Remember to verify that the format
                            is correct.
                        </label>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputQuery" className="common-label">If you wish, you can also obtain
                            the solution to this exercise by consulting the database:</label>
                        <CommandLineComponent func={this.onExecute} rows={6}/>
                    </div>
                    <div align="center" className="form-group">
                        <button type="submit" className="btn btn-danger common-button"
                                id="cancelButton">Cancel Exercise
                        </button>
                        <button type="submit" className="btn btn-success common-button" id="submitButton">Submit
                            Exercise
                        </button>
                    </div>
                </form>
            </div>
        );
    }
});

export default ExerciseCreationFormComponent;