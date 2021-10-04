import {Extra} from '../models/extra';
import {Size} from '../models/size';
import {CoffeeMachineSliceType} from '../redux/coffee_machine/coffee_machine_slice';

export const getSizes = (data: CoffeeMachineSliceType): Size[] => {
  const pickedType = data.pickedType.type;
  return data.coffeeMachine.sizes.filter((element: Size) =>
    pickedType?.sizes.includes(element._id),
  );
};
export const getExtras = (data: CoffeeMachineSliceType): Extra[] => {
  const pickedType = data.pickedType.type;
  return data.coffeeMachine.extras.filter((element: Extra) =>
    pickedType?.extras.includes(element._id),
  );
};
