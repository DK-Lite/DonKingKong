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

    let dataName = "";
    if (data.length > 0){
        dataName = data[0].apt_name;
    }
    const dataLists = data.map( x => 
        ({
            ymd: x.trade_year+"-"+pad(x.trade_month, 2)+"-"+pad(x.trade_day, 2),
            value: x.trade_value,
            area: x.dedicated_area,
        }))

    return (
       
            <MaterialTable
            maxBodyHeight='660px'
            style={{ width: '380px', height: '660px', zIndx: 0}}
            title={dataName}
            columns={[
                { title: 'Date', field: 'ymd' },
                { title: 'Price', field: 'value' },
                { title: 'Area', field: 'area' },
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
    )
}


export default connect(
    state => state.map,
    null
)(TradeTable)

