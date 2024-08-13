#!/usr/bin/node
// Import the File System module
const fs = require('fs');

// Read the file passed as the first command-line argument
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Log the error if it occurs, otherwise log the file content
  console.log(error || content);
});
