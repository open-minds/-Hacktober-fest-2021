import {createSlice} from '@reduxjs/toolkit';

import {
  FETCHING_COFFEE,
  FETCHING_COFFEE_FAILURE,
  FETCHING_COFFEE_IDLE,
  FETCHING_COFFEE_SUCCESS,
} from '../../utils/constants';

import {fetchCoffeeMachine} from './thunks';

import {getExtras, getSizes} from '../../utils/helpers';
import {Coffee, CoffeeMachine, FinalCoffee} from '../../models';

export type CoffeeMachineSliceType = {
  coffeeMachine: CoffeeMachine;
  pickedType: Coffee;
  finalCoffee: FinalCoffee;
  status: string;
  error: string;
};
const initialState: CoffeeMachineSliceType = {
  coffeeMachine: {
    _id: null,
    extras: [],
    sizes: [],
    types: [],
  },
  pickedType: {
    type: null,
    sizes: [],
    extra: [],
  },
  finalCoffee: {
    type: {
      id: null,
      name: null,
    },
    size: null,
    extras: null,
  },
  status: FETCHING_COFFEE_IDLE,
  error: '',
};

export const coffeeMachineSlice = createSlice({
  name: 'coffeeMachineSlice',
  initialState,
  reducers: {
    pickCoffeeType(state, action) {
      //setting the picked coffee data to pick from

      state.pickedType.type = action.payload;
      state.pickedType.sizes = getSizes(state);
      state.pickedType.extra = getExtras(state);
      //Setting up the final Coffee that we will send to the machine
      state.finalCoffee.type.id = action.payload.id;
      state.finalCoffee.type.name = action.payload.name;
    },
    pickCoffeeSize(state, action) {
      state.finalCoffee.size = action.payload;
    },
  },
  extraReducers: builder => {
    builder.addCase(fetchCoffeeMachine.fulfilled, (state, action) => {
      state.status = FETCHING_COFFEE_SUCCESS;
      state.coffeeMachine = action.payload!;
    });
    builder.addCase(fetchCoffeeMachine.pending, state => {
      state.status = FETCHING_COFFEE;
    });
    builder.addCase(fetchCoffeeMachine.rejected, (state, action) => {
      state.status = FETCHING_COFFEE_FAILURE;
      state.error = action.payload as string;
    });
  },
});
export const {pickCoffeeType, pickCoffeeSize} = coffeeMachineSlice.actions;
export default coffeeMachineSlice.reducer;
