import React, { Component } from 'react';
import {BootstrapTable,
    TableHeaderColumn} from 'react-bootstrap-table';

class LeaderboardTableComponent extends Component {
    render() {
        return (
            <div>
                <BootstrapTable data={this.props.data}
                                tableStyle={ { border: '#ffa54c 1.5px solid'} }
                                trClassName="common-label">
                    <TableHeaderColumn isKey dataField='position' dataAlign='center' width='150'>
                        <label className="common-label">Ranking</label>
                    </TableHeaderColumn>
                    <TableHeaderColumn dataField='nickname' dataAlign='center' width='150'>
                        <label className="common-label">Nickname</label>
                    </TableHeaderColumn>
                    <TableHeaderColumn dataField='score' dataAlign='center' width='150'>
                        <label className="common-label">Score</label>
                    </TableHeaderColumn>
                </BootstrapTable>
            </div>
        );
    }
}

export default LeaderboardTableComponent;