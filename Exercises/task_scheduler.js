/*
You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.
You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.
Each day, until all tasks have been completed, you must either:
Complete the next task from tasks, or take a break.
Return the minimum number of days needed to complete all tasks.
*/

function solution (array, space) {
  const map = new Map();
  var sol = 0;
  for (let i = 0; i < array.length; i++) {
    if (!map.get(array[i])) {
      map.forEach((value, key) => {
      map.set(key, value-1)
      });
      map.set((array[i]), space)
      sol++
      console.log(map)
      continue;
    }
    if (map.get(array[i]) <= 0) {
      map.forEach((value, key) => {
      map.set(key, value-1)
      });
      map.set((array[i]), space)
      sol++
      continue;
          console.log(map)
    }
    else {
      map.forEach((value, key) => {
        map.set(key, value-1)
      });
    
      i--
    console.log(map)
    sol++
    }
  }
  return sol
}

console.log(solution([1,2,1,2,3,1], 3))
console.log(solution([5,8,8,5], 2))