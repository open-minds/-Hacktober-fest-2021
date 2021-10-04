import {Extra} from './extra';
import {Size} from './size';
import {Type} from './type';

export interface Coffee {
  type: Type | null;
  sizes: Size[];
  extra: Extra[];
}
