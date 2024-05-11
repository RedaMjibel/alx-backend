#!/usr/bin/env node

import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redisPrint);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (_err, reply) => {
    console.log(reply);
  });
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
