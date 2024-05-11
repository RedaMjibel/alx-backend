#!/usr/bin/env node

import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redisPrint);
};

const displaySchoolValue = async (schoolName) => {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.error('Error:', error);
  }
};

const redisPrint = (err, reply) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('Reply:', reply);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

