/*
Given an object, return a valid JSON string of that object. 
You may assume the object only inludes strings, integers, arrays, objects, booleans, and null. 
The returned string should not include extra spaces. 
The order of keys should be the same as the order returned by Object.keys().
*/
function arrayStringify(array) {
  let output = "[";

  for (let i = 0; i < array.length; i++) {
    if (typeof array[i] == "string") {
      output = output.concat("\"" + array[i] + "\"");
    } else if (typeof array[i] == "boolean") {
      output = output.concat(array[i].toString());
    } else if (array[i] == null) {
      output = output.concat("null");
    } else if (Array.isArray(array[i])) {
      output = output.concat(arrayStringify(array[i]));
    } else if (typeof array[i] == "object") {
      output = output.concat(jsonStringify(array[i]));
    } else {
      output = output.concat(array[i]);
    }
    if (i < array.length - 1) {
      output = output.concat(",");
    }
  }
  output = output.concat("]");
  return output;
}

function jsonStringify(object) {
  if (object == true || object == false) {
    return object.toString();
  }

  const keys = Object.keys(object);
  let output = "{";

  for (let i = 0; i < keys.length; i++) {
    output = output.concat("\"" + keys[i] + "\"" + ":");
    // Check value for string
    if (typeof object[keys[i]] == "string") {
      output = output.concat("\"" + object[keys[i]] + "\"");
    }
    // Check value for null
    else if (object[keys[i]] == null) {
      output = output.concat("null");
    }
    // Check value for array
    else if (Array.isArray(object[keys[i]])) {
      output = output.concat(arrayStringify(object[keys[i]]));
    }
    // Check value for object 
    else if (typeof object[keys[i]] == "object") {
      output = output.concat(jsonStringify(object[keys[i]]));
    }
    // Add value to output string
    else {
      output = output.concat(object[keys[i]]);
    }
    // Add comma after adding each value to output
    if (i < keys.length - 1) {
      output = output.concat(",");
    }
  }
  output = output.concat("}");

  return output;
}

const input1 = {"y":1,"x":2};
const input2 = {"a":"str","b":-12,"c":true,"d":null};
const input3 = {"key":{"a":1,"b":[{},null,"Hello"]}};
const input4 = true;
const input5 = {"1":[true,1]};

console.log(jsonStringify(input1));
console.log(jsonStringify(input2));
console.log(jsonStringify(input3));
console.log(jsonStringify(input4));