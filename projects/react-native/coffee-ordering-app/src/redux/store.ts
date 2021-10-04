import {configureStore} from '@reduxjs/toolkit';
import coffeeMachineSlice from './coffee_machine/coffee_machine_slice';
export const store = configureStore({
  reducer: coffeeMachineSlice,
});
export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
