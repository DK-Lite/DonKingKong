import React from 'react';

// Redux
import { connect } from 'react-redux'

// Material-UI
import MaterialTable from 'material-table';

function pad(n, width) {
    n = n + '';
    return n.length >= width ? n : new Array(width - n.length + 1).join('0') + n;
  }


function TradeTable(props){
    const { data } = props;

    const dataLists = data.map( x => 
        ({
            ymd: x.trade_year+"-"+pad(x.trade_month, 2)+"-"+pad(x.trade_day, 2),
            value: x.trade_value,
            area: x.dedicated_area,
        }))

    return (
        <div style={{ width: '700px'}}>
            <MaterialTable
            maxBodyHeight='660px'
            style={{ height: '660px'}}
            title={"신당역솔하임"}
            columns={[
                { title: '거래 일', field: 'ymd' },
                { title: '거래 가격', field: 'value' },
                { title: '면적', field: 'area' },
            ]}
            data={dataLists}
            options={{
                filtering: false,
                pageSize:8,
                pageSizeOptions: [8],
                search: false,
                showFirstLastPageButtons: false,
                sorting: true,
              }}      
            />
        </div>
    )
}


export default connect(
    state => state.map,
    null
)(TradeTable)

