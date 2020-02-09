// Standard
import React from 'react';
import styled from 'styled-components';

// Custom
import Map from './Map';
import TradeTable from './TradeTable';

// Redux
import { connect } from 'react-redux';




const RootDiv = styled.div`
    width: 100%;
    min-height: 100vh;
    background: white;
    display: flex;
    justify-content: flex-start;
`
const MenuDiv = styled.div`
    width: 100%;
    height: 50px;
    background: #000624;
    padding: 0px 0px 0px 20px;
    position: fixed;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    z-index: 1;
`
const MainDiv = styled.div`
    width: 100%;
    background: white;
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
`

const ContentsDiv = styled.div`
    padding: 70px 0px 0px 0px;
    width: 100%;
    display: flex;
    justify-content: center;
`

const MapDiv = styled.div`
    padding: 10px;
    background: white;
    display: flex;
    justify-content: flex-end;
`

const InfoDiv = styled.div`
    background: white;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
`
const AnalyDiv = styled.div`
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-flow: column wrap;
`
const CustomMenu = styled.div`
    width: 70px;
    height : 50px;
    background: #ECECF0;
    align-items: center;
    text-align: center;
`

const CustomCard = styled.div`
    width: 670px;
    height: 200px;
    background: white;
    border: 1px dotted;
    border-radius: 10px;
    margin: 10px 10px 0px;
    padding: 5px;
`
const ChartCard = styled.div`
    width: 1400px;
    height: 400px;
    background: white;
    border: 1px dotted;
    border-radius: 10px;
    padding: 10px 0px 0px 0px;
`



function MainView(props){
    const { data } = props; // state
    console.log(data)
 
    return (
        <RootDiv>
            <MenuDiv>
                <CustomMenu> Menu </CustomMenu>
            </MenuDiv>
            <MainDiv>
                <ContentsDiv>
                    <MapDiv>
                        <Map></Map>
                    </MapDiv>
                    <InfoDiv>
                        <TradeTable/>
                    </InfoDiv>
                </ContentsDiv>
                <AnalyDiv>
                    <ChartCard></ChartCard>
                </AnalyDiv>
            </MainDiv>
        </RootDiv>
    )
}

export default connect(
    state => state.map,
    null
)(MainView)
//export default MainView;