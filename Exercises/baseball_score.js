
let score = [];

const operations = {
  'C': () => score.pop(),
  'D': () => score.push(2 * score[score.length - 1]),
  '+': () => score.push(score[score.length - 1] + score[score.length - 2])
}

function callPts(ops) {
  for (let i = 0; i < ops.length; i++) {
    if (ops[i] in operations) {
      operations[ops[i]]();
    } else {
      score.push(parseInt(ops[i]));
    }
  }
  return score.reduce((accum, value) => accum + value, 0);
}

function calPoints(ops) {

  for (let i = 0; i < ops.length; i++) {

    if (ops[i] === '+') {
      score.push(score[score.length - 1] + score[score.length - 2])
    }
    else if (ops[i] === 'D') {
      score.push(2 * score[score.length - 1]);
    }
    else if (ops[i] === 'C') {
      score.pop();
    }
    else {
      score.push(parseInt(ops[i]));
    }
  }
  return score.reduce((accum, value) => accum + value, 0);
}

let ex1 = ["5", "2", "C", "D", "+"];
console.log(callPts(ex1));


let crazyNumber = [1, 2, 3, 4];
// console.log(crazyNumber.reduce((accum, value) => accum + value, 0));



