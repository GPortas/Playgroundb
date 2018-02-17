import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseCreationFormComponent = createReactClass({
    changeHandler(solutionText) {
        $("#inputSolution").val(solutionText);
    },

    componentDidMount() {
        $("#submitButton").click(function(){
            $('#submitButton').attr('disabled', true);
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
                complete: function () {
                    $('#submitButton').attr('disabled', false);
                }
                //todo: Errors treatment!
            });
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
                        <CommandLineComponent func={this.changeHandler}/>
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