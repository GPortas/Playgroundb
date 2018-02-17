import '../../styles/App.css';
import $ from 'jquery';

var React = require('react');
var createReactClass = require('create-react-class');

const CommandLineComponent = createReactClass({
    componentDidMount() {
        const self = this;
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
                success: function(output, status, xhr) {
                    const data=xhr.responseText;
                    const jsonResponse = $.parseJSON(data);
                    self.setState({ data: jsonResponse["data"]["execution_result"] });
                },
                complete: function () {
                    $('#executeQueryButton').attr('disabled', false);
                }
                //todo: Errors treatment!
            });
        });
    },
    render() {
        if (this.state && this.state.data) {
            this.props.func(this.state.data)
        }
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