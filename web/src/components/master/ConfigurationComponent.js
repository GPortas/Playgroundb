import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'
import {generateAuthHeader} from "../../utils/utils";

var React = require('react');
var createReactClass = require('create-react-class');

const ConfigurationComponent = createReactClass({
    onExecute(inputQuery) {
        $('#executeQueryButton').attr('disabled', true);
        var formData = {
            "query": inputQuery,
        }
        $.ajax({
            url: process.env.REACT_APP_BASE_URL + "/query-execution/",
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
        return (
            <div className="common-div App">
                <label className="common-label">Write and execute queries in the following console:</label>
                <CommandLineComponent func={this.onExecute} rows={6}/>
                <label className="common-label">Result:</label>
                <textarea readOnly={true} className="form-control query-text-area" id="queryOutput" rows={16}/>
            </div>
        );
    }
});

export default ConfigurationComponent;