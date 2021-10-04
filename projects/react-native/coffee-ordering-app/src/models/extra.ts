import {SubSelection} from './subselection';

export interface Extra {
  _id: string;
  name: string;
  subselections: SubSelection[];
}
