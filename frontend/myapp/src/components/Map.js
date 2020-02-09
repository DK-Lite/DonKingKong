import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styled from 'styled-components';

//Redux
import { connect } from 'react-redux';
import { actions as mapActions } from '../ducks/Map';

declare var kakao:any;

const CustomMap = styled.div`
    width: 700px;
    height: 660px;
    border: 0px dotted;
    border-radius: 15px;
    z-index: 0;
`

function Map(props){
    const { data } = props // state
    const { setData } = props // actions

    const [tmp, setTmp] = useState([]);
    const [kakaoMap, setkakaoMap] = useState();
    const [dataList, setdataList] = useState([]);
    
    useEffect(()=>{
        getAptUniqueInfo()
    },[])


    useEffect(()=>{
        const el = document.getElementById('map');
        
        const positions = tmp.map( data => ({ 
            title: data.apt_name,
            latlng: new kakao.maps.LatLng(data.latitudes, data.longitude),
            road_city_code: data.road_city_code,
            road_code: data.road_code,
        }))
         
        var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
        var imageSize = new kakao.maps.Size(24, 35);
          
        // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize)
    
        var kamap = new kakao.maps.Map(el, {
            center: new kakao.maps.LatLng(37.563642596447494, 127.0260017409586),
        });
    
        for(var i = 0; i < positions.length; i ++) {
            var marker = new kakao.maps.Marker({
                map: kamap, // 마커를 표시할 지도
                position: positions[i].latlng,
                title : positions[i].title,
                image : markerImage,  
                content: positions[i].road_city_code, 
    
            });
            var uniqueKey = ({
                road_city_code: positions[i].road_city_code,
                road_code : positions[i].road_code,
            });

            (function(marker, uniqueKey) {
                kakao.maps.event.addListener(marker, 'click', function() {
                    getAptInfo(uniqueKey)
                });
            })(marker, uniqueKey);

        }
        setkakaoMap(kamap)
    },[tmp])


    const getAptUniqueInfo=()=>{
        axios.get("http://34.84.195.184:3691/data-warehouse/apt-unique-info")
        .then(response => setTmp(response.data.info))
        .catch(error => console.log(error))
    }

    const getAptInfo=(uniqueKey)=>{
        axios.post("http://34.84.195.184:3691/data-warehouse/apt-unique-info/apt-info", uniqueKey)
        .then(response => setData(response.data.info))
        .catch(error => console.log(error))
    }
   
    return (
        <React.Fragment>
            <CustomMap className='Map' id="map" />

        </React.Fragment>
    )

}


export default connect(
    state => state.map,
    mapActions
)(Map);
//export default Map;