import {Extra} from './extra';
import {Size} from './size';

export interface FinalCoffee {
  type: {
    id: string | null;
    name: string | null;
  };
  size: Size | null;
  extras: Extra | null;
}
