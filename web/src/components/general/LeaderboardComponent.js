import '../../styles/App.css';
import $ from 'jquery';
import {generateAuthHeader} from "../../utils/utils";
import LeaderboardTableComponent from "./LeaderboardTableComponent";
import {Component} from "react";

var React = require('react');

class LeaderboardComponent extends Component {
    constructor(props) {
        super(props);
        this.getFormattedUsersList = this.getFormattedUsersList.bind(this);
    }

    componentWillMount() {
        const self = this;
        $.ajax({
            url: process.env.REACT_APP_BASE_URL + "/users/",
            dataType: 'json',
            type: 'get',
            headers: generateAuthHeader(),
            crossDomain: true,
            success: function (output, status, xhr) {
                const data = xhr.responseText;
                const jsonResponse = $.parseJSON(data);
                self.setState({users: self.getFormattedUsersList(jsonResponse["data"])});
            },
            complete: function () {
            }
            //todo: Errors treatment!
        });
    }

    getFormattedUsersList(responseData) {
        const formattedData = [];
        responseData.forEach(function (value, i) {
            formattedData.push({"position": i+1, "nickname": value["nickname"], "score": value["score"]});
        });
        return formattedData;
    }

    render() {
        if (this.state && this.state.users) {
            return (
                <div className="common-div">
                    <label className="exercise-section-title-label">Leaderboard</label>
                    <LeaderboardTableComponent data={this.state.users}/>
                </div>
            );
        } else {
            return (
                <div className="common-div">
                </div>
            );
        }
    }
}

export default LeaderboardComponent;