import {client} from '../api/client';

export const getCoffeeMachineById = async (id: string) => {
  const response = await client.get(`/coffee-machine/${id}`, {});
  return response;
};
