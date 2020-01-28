import * as React from 'react';

declare var daum:any;

const styler = {
    map :{
        width: "100%",
        height: "400px",
        float: "left",
    },
}
class Map extends React.Component {

    componentDidMount() {
        const el = document.getElementById('map');
        let daumMap = new daum.maps.Map(el, {
            center: new daum.maps.LatLng(33.450701, 126.5700667),
        });
    }
    
    
    render() {
        return (
            <React.Fragment>
                <div className='Map' id="map" style={styler.map}/>
            </React.Fragment>
        )
    }
}


export default Map;