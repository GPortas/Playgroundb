import '../../styles/App.css';
import $ from 'jquery';
import CommandLineComponent from '../general/CommandLineComponent'

var React = require('react');
var createReactClass = require('create-react-class');

const ConfigurationComponent = createReactClass({
    changeHandler(solutionText) {
        $("#queryOutput").val(solutionText);
    },

    render() {
        return (
            <div className="common-div App">
                <label className="common-label">Write and execute queries in the following console:</label>
                <CommandLineComponent func={this.changeHandler} rows={6}/>
                <label className="common-label">Result:</label>
                <textarea readOnly={true} className="form-control query-text-area" id="queryOutput" rows={16}/>
            </div>
        );
    }
});

export default ConfigurationComponent;