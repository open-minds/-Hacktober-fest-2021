import {Size} from '../../models/size';

export const selectAllTypes = (state: any) => state.coffeeMachine.types;

export const getError = (state: any) => {
  return state.error;
};
export const f = (state: {sizes?: string[]}, sizes: Size[]) => {
  return sizes.filter((element: Size) => state.sizes?.includes(element._id));
};
