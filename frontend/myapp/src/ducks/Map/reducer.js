import * as types from './constants';

const initState = {
    data: [],
}


function reducer(state = initState, action){
    switch(action.type){
        case types.SET_DATA_LIST:
            return {
                ...state,
                data: action.payload,
            }
        default: 
            return { ...state }
    }

}

export default reducer;