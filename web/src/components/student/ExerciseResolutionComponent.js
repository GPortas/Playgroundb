import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'

var React = require('react');
var createReactClass = require('create-react-class');

const ExerciseResolutionComponent = createReactClass({
    componentWillMount() {
        const self = this;
        $.ajax({
            url: "http://127.0.0.1:8000/exercises/",
            dataType: 'json',
            type: 'get',
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
                url: "http://127.0.0.1:8000/exercises/correct-exercise/",
                dataType: 'json',
                type: 'post',
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

    changeHandler(solutionText) {
        $("#queryOutput").val(solutionText);
    },

    render() {
        if (this.state && this.state.exercises) {
            return (
                <div>
                    <div className="common-div">
                        <div className="exercise-resolution-left-div">
                            <label className="common-label">Statement:</label>
                            <hr className="exercise-resolution-divider"/>
                            <label className="common-label">
                                {this.state.exercises[0]["question"]}
                            </label>
                            <div className="exercise-resolution-left-bottom-div">
                                <CommandLineComponent func={this.changeHandler} rows={6}/>
                            </div>
                        </div>
                        <div className="exercise-resolution-right-div">
                            <label className="common-label">Solution:</label>
                            <textarea readOnly={true} className="form-control query-text-area" id="queryOutput"
                                      rows={18}/>
                            <button type="submit" className="btn btn-success common-button" id="submitButton">Submit
                                Solution
                            </button>
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