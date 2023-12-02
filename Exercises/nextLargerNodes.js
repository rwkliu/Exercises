// Topic: Next Greatest Node in Linked List


// You are given the head of a linked list with n nodes.
// For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.
// Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

// Example 1:

const list1 = {
  value: 2,
  next: {
    value: 1,
    next: {
      value: 5,
      next: null
    }
  }
};

// Input: head = [2,1,5]
// Output: [5,5,0]

// Example 2:


const list2 = {
  value: 2,
  next: {
    value: 7,
    next: {
      value: 4,
      next: {
        value: 3,
        next: {
          value: 5,
          next: null
        }
      }
    }
  }
};
// Input: head = [2,7,4,3,5]
// Output: [7,0,5,5,0]

// Constraints:
// The number of nodes in the list is n.
// 1 <= n <= 104
// 1 <= Node.val <= 109

const checkNext = (current, next, output) => {
  if (current.next === null) {
    output.push(0)
    return
  }

  if (next === null) {
    output.push(0)
    return checkNext(current.next, current.next.next, output)
  }
  
  if (current.value >= next.value) {
    return checkNext(current, next.next, output)
  } else if (current.value < next.value) {
    output.push(next.value)
    return checkNext(current.next, current.next.next, output)
  }
}

// Prototype in JS (you can do this in any language)
function nextLargerNodes(head) {
  const output = []
  checkNext(head, head.next, output)
  console.log(output)
}



nextLargerNodes(list1)
nextLargerNodes(list2)