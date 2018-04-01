import '../../styles/App.css';
import $ from 'jquery';
import {encryptCookieName, generateAuthHeader} from "../../utils/utils";

var React = require('react');
var createReactClass = require('create-react-class');

const CommandLineComponent = createReactClass({
    componentDidMount() {
        const self = this;
        $("#executeQueryButton").click(function(){
            self.setState({ inputQuery: $('#inputQuery').val() });
        });
    },
    render() {
        if (this.state && this.state.inputQuery) {
            this.props.func(this.state.inputQuery)
        }
        return (
            <div>
                <textarea className="form-control query-text-area" id="inputQuery" rows={this.props.rows}/>
                <button type="submit" className="btn btn-warning common-button"
                        id="executeQueryButton">Execute Query
                </button>
            </div>
        );
    }
});

export default CommandLineComponent;