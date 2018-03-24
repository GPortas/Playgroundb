import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils";

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
                        <textarea type="statement" className="form-control input-text" id="inputStatement"
                                  aria-describedby="statement" rows="6"/>
                        <label id="statementHelp" className="form-text text-muted">Try to be as concise as possible
                            because this will be the statement that your students will receive.
                        </label>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputSolution" className="common-label">Write the expected result
                            after executing the necessary query:</label>
                        <textarea type="solution" className="form-control input-text" id="inputSolution" rows="6"
                                  placeholder={"{\"data\": {}}"}/>
                        <label id="solutionHelp" className="form-text text-muted">Remember to verify that the format
                            is correct.
                        </label>
                    </div>
                    <div className="form-group">
                        <label htmlFor="inputQuery" className="common-label">If you wish, you can also obtain
                            the solution to this exercise by consulting the database:</label>
                        <CommandLineComponent func={this.changeHandler} rows={6}/>
                    </div>
                    <div align="center" className="form-group">
                        <button type="submit" className="btn btn-danger common-button"
                                id="cancelButton">Cancel Exercise
                        </button>
                        <button type="submit" className="btn btn-success common-button" id="submitButton">Submit Exercise</button>
                    </div>
                </form>
            </div>
        );
    }
});

export default ExerciseCreationFormComponent;