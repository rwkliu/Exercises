// Given a list of three points in the plane, return whether these points are a boomerang.
// A boomerang is a set of 3 points that are all distinct and not in a straight line.

function calculate_slope(arr1, arr2) {
  const [x, y] = arr1;
  const [x1, y1] = arr2;
  return (y1 - y) / (x1 - x);
}

function valid_boomerang(param_1) {
  const result = []; 
  for (let i = 0; i < param_1.length - 1; i++) {
    let points = calculate_slope(param_1[i], param_1[i+1]);
    result.push(points);
  }
  for (let j = 0; j < result.length - 1; j++) {
    if(result[j] == result[j+1]) {
      return false;
    }
  }
  return true;
}

let input1 = [[1, 1], [2, 3], [3, 2]];
let input2 = [[1, 1], [2, 2], [3, 3]];

console.log(valid_boomerang(input1));
console.log(valid_boomerang(input2));