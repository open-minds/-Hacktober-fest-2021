import {createAsyncThunk} from '@reduxjs/toolkit';
import {getCoffeeMachineById} from '../../services/coffee_api';
import {
  COFFEE_MACHINE_NOT_FOUND,
  COFFEE_MACHINE_SERVER_ERROR,
  FETCHING_COFFEE,
  FETCHING_COFFEE_SUCCESS,
} from '../../utils/constants';

export const fetchCoffeeMachine = createAsyncThunk(
  'coffeeMachine',
  async (id: string, {rejectWithValue}) => {
    try {
      const response = await getCoffeeMachineById(id);
      return response;
    } catch (error) {
      switch (error) {
        case '404':
          return rejectWithValue(COFFEE_MACHINE_NOT_FOUND);

        case '500':
          return rejectWithValue(COFFEE_MACHINE_SERVER_ERROR);
        default:
          return rejectWithValue('Something is wrong with the connection');
      }
    }
  },
  {
    condition: (_, {getState}) => {
      const state = getState() as any;
      const status = state.status;
      if (status === FETCHING_COFFEE_SUCCESS || status === FETCHING_COFFEE) {
        return false;
      }
    },
  },
);
