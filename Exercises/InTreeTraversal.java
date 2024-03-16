import java.util.*;


class Main {
  public static class Node {
      int value;
      Node left;
      Node right;
  
      Node(int value) {
          this.value = value;
          right = null;
          left = null;
      }
  }
  public static void main(String[] args) {
    Node start = new Node(0);
    Node node1 = new Node(1);
    Node node2 = new Node(2);
    Node node3 = new Node(3);
    Node node4 = new Node(4);
    Node node5 = new Node(5);
    Node node6 = new Node(6);
    start.left = node1;
    start.right = node2;
    node1.left = node3;
    node1.right = node4;
    node2.left = node5;
    node2.right = node6;

    System.out.println(inTree(start, 3));
    System.out.println(inTree(start, 8));
    System.out.println(inTree(start, 0));
  }

  /*
   * Traverse the tree as far down one branch before moving to the next branch 
   * (depth first search). 
   * Time complexity: O(n) where n is the height of the tree
   * Memory complexity: O(n) where n is the height of the tree. Worst case is 
   * when the entire tree is pushed onto the stack
   */
  public static boolean inTree(Node tree, int target) {
    // The stack keeps track of the seen nodes, where the top of the stack is 
    // the most recent node
    Stack<Node> stack = new Stack<>();
    Node curr = tree;

    // Check the first node for the target value
    if (curr.value == target) {
      return true;
    }
    // Traverse the tree until either the target is found or the stack is empty,
    // meaning all nodes have been visited
    while (curr != null || !stack.empty()) {
      // Push the nodes to the left of the current node until end of tree is reached
      while (curr != null) {
        stack.push(curr);
        curr = curr.left;
      }
      curr = stack.pop();
      // Check the current node for the target value
      if (curr.value == target) {
        return true;
      }
      curr = curr.right;
    }
    return false;
  }
  
}