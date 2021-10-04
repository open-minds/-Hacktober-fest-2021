import {Type} from './type';
import {Size} from './size';
import {Extra} from './extra';

export interface CoffeeMachine {
  _id: string | null;
  extras: Extra[];
  sizes: Size[];
  types: Type[];
}
