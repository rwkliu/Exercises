class ListNode {
  int val;
  ListNode next;
  ListNode() {}
  ListNode(int val) { this.val = val;}
  ListNode(int val, ListNode next) { this.val = val; this.next = next;}
}
public class ReverseLinkedList {

  public static ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;
    ListNode next = null;

    while (curr != null) {
        next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    ListNode node2 = new ListNode(2);
    ListNode node3 = new ListNode(3);
    ListNode node4 = new ListNode(4);
    ListNode node5 = new ListNode(5);
    head.next = node2;
    node2.next = node3;
    node3.next = node4;
    node4.next = node5;
    ListNode curr = reverseList(head);
    while (curr != null) {
      System.out.println(curr.val);
      curr = curr.next;
    }
  }
}