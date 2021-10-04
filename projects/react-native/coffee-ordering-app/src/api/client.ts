// @ts-nocheck why : just for the sake of time : )
import {BASE_URL} from '../utils/constants';

export async function client(
  endpoint: string,
  {body, ...customConfig}: {body: any; customConfig: any},
) {
  const headers = {'Content-Type': 'application/json'};

  const config = {
    method: body ? 'POST' : 'GET',
    ...customConfig,
    headers: {
      ...headers,
      ...customConfig.headers,
    },
  };

  if (body) {
    config.body = JSON.stringify(body);
  }

  let data;
  try {
    const response = await fetch(endpoint, config);
    data = await response.json();
    if (response.ok) {
      return data;
    }
    throw new Error(response.status);
  } catch (err) {
    return Promise.reject(err.message ? err.message : data);
  }
}

client.get = function (endpoint: string, customConfig: any) {
  return client(BASE_URL + endpoint, {...customConfig, method: 'GET'});
};

client.post = function (endpoint: string, body: any, customConfig: any) {
  return client(BASE_URL + endpoint, {...customConfig, body});
};
