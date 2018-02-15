import '../../styles/App.css';
import $ from 'jquery';

var React = require('react');
var createReactClass = require('create-react-class');

const CommandLineComponent = createReactClass({
    componentDidMount() {
        $("#executeQueryButton").click(function(){
            $('#executeQueryButton').attr('disabled', true);
            const inputQuery = $('#inputQuery').val();
            var formData = {
                "query": inputQuery,
            }
            $.ajax({
                url: "http://127.0.0.1:8000/query-execution/execute-query/",
                type: 'post',
                dataType: 'json',
                data: formData,
                success: function(data) {
                    window.alert("execute query clicked!");
                },
                complete: function () {
                    $('#executeQueryButton').attr('disabled', false);
                },
                error: function (jqXHR, exception) {
                if (jqXHR.status === 0) {
                    alert('Not connect.\n Verify Network.');
                } else if (jqXHR.status == 404) {
                    alert('Requested page not found. [404]');
                } else if (jqXHR.status == 500) {
                    alert('Internal Server Error [500].');
                } else if (exception === 'parsererror') {
                    alert('Requested JSON parse failed.');
                } else if (exception === 'timeout') {
                    alert('Time out error.');
                } else if (exception === 'abort') {
                    alert('Ajax request aborted.');
                } else {
                    alert('Uncaught Error.\n' + jqXHR.responseText);
                }
            }
            });
        });
    },
    render() {
        return (
            <div>
                <textarea type="query" className="form-control queryTextArea" id="inputQuery" rows="6"/>
                <button type="submit" className="btn btn-warning exercise-creation-execute-query-button"
                        id="executeQueryButton">Execute Query
                </button>
            </div>
        );
    }
});

export default CommandLineComponent;