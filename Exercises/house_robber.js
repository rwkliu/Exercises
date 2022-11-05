/*
gotta start with the house that has the highest amount of cash unless the sum of those of its neighbors is worth more maybe
idk
or compare the sums of odd and even houses and go for the highest
*/

// Recursion way
function f(ind, nums, dp)
{

    if (ind < 0)
        return 0;

        if (dp[ind]) {
        return dp[ind];
    }

    let pick = nums[ind] + f(ind - 2, nums, dp);
    let notPick = 0 + f(ind - 1, nums, dp);

    return dp[ind] = Math.max(pick, notPick);
}

var rob2 = function(nums) {
    let memo = {};
    return f(nums.length - 1, nums, memo);
}

// loop + sum way
var rob = function(nums) {
    let prevSum3 = 0;
    let prevSum2 = 0;
    let prevSum1 = 0;
    
    for (let i = 0; i < nums.length; i++) {
        let sum = Math.max(nums[i]+prevSum2, nums[i]+prevSum3);
        prevSum3 = prevSum2;
        prevSum2 = prevSum1;
        prevSum1 = sum;
    }
    
    return Math.max(prevSum3, prevSum2, prevSum1);
};

  
  console.log(rob2([2,7,9,3,1]))