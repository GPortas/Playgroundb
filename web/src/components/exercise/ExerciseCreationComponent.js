import '../../styles/App.css';
import $ from 'jquery';

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseCreationFormComponent = createReactClass({
    componentDidMount() {
        $("#submitButton").click(function(){
            console.log("submit clicked!");
            window.alert("submit clicked!");
            const exerciseStatement = $('#inputStatement').val();
            const exerciseSolution = $('#inputSolution').val();
            var formData = {
                    "author": "testauthor",
                    "question": exerciseStatement,
                    "solution": exerciseSolution
            }
            $.ajax({
                url: "http://127.0.0.1:8000/exercises/",
                dataType: 'json',
                type: 'post',
                data: formData,
                crossDomain: true,
                success: function(data) {
                    window.alert('yeah');
                },
                error: function(jqXHR, exception) {
                    if (jqXHR.status === 0) {
                        window.alert('Not connect.\n Verify Network.');
                    } else if (jqXHR.status == 404) {
                        window.alert('Requested page not found. [404]');
                    } else if (jqXHR.status == 500) {
                        window.alert('Internal Server Error [500].');
                    } else if (exception === 'parsererror') {
                        window.alert('Requested JSON parse failed.');
                    } else if (exception === 'timeout') {
                        window.alert('Time out error.');
                    } else if (exception === 'abort') {
                        window.alert('Ajax request aborted.');
                    } else {
                        window.alert('Uncaught Error.\n' + jqXHR.responseText);
                    }
                }
            });
        });

        $("#executeQueryButton").click(function(){
            console.log("execute query clicked!");
            window.alert("execute query clicked!");
        });
    },
    render() {
        return (
            <div className="exercise-creation-forms-div">
                <form>
                    <div className="form-group">
                        <label htmlFor="inputStatement" className="exercise-creation-label">Write the statement of the
                            exercise:</label>
                        <textarea type="statement" className="form-control" id="inputStatement"
                                  aria-describedby="statement" rows="3"/>
                        <small id="statementHelp" className="form-text text-muted">Try to be as concise as possible
                            because this will be the statement that your students will receive.
                        </small>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputSolution" className="exercise-creation-label">Write the expected result
                            after executing the necessary query:</label>
                        <textarea type="solution" className="form-control" id="inputSolution" rows="3"
                                  placeholder={"{\"data\": {}}"}/>
                        <small id="solutionHelp" className="form-text text-muted">Remember to verify that the format
                            is correct.
                        </small>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputQuery" className="exercise-creation-label">If you wish, you can also obtain
                            the solution to this exercise by consulting the database:</label>
                        <textarea type="query" className="form-control queryTextArea" id="inputQuery" rows="6"/>
                        <button type="submit" className="btn btn-warning exercise-creation-execute-query-button"
                                id="executeQueryButton">Execute Query
                        </button>
                    </div>
                    <div align="center" className="form-group">
                        <button type="submit" className="btn btn-danger exercise-creation-execute-cancel-button"
                                id="cancelButton">Cancell Exercise
                        </button>
                        <button type="submit" className="btn btn-success" id="submitButton">Submit Exercise</button>
                    </div>
                </form>
            </div>
        );
    }
});

export default ExerciseCreationFormComponent;