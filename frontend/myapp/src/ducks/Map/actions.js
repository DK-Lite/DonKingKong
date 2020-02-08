import * as types from './constants'

export const setData = data => ({
    type: types.SET_DATA_LIST,
    payload: data,
})