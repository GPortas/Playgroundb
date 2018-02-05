import '../../styles/App.css';
import $ from 'jquery';

var React = require('react');
var createReactClass = require('create-react-class');

const CommandLineComponent = createReactClass({
    componentDidMount() {
        $("#executeQueryButton").click(function(){
            console.log("execute query clicked!");
            window.alert("execute query clicked!");
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