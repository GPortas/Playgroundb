import '../../styles/App.css';

var React = require('react');
var createReactClass = require('create-react-class');

const ContainerComponent = createReactClass({
    render() {
        return (
            <div className="App">
                {this.props.nestedComponent}
            </div>
        );
    }
});

export default ContainerComponent;