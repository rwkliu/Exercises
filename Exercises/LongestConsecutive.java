import java.util.Set;
import java.util.HashSet;

class LongestConsecutive{
  public static void main(String[] args) {
    int[] nums = {100,4,200,1,3,2};
    int[] nums2 = {0,3,7,2,5,8,4,6,0,1};
    
    System.out.println(longestConsecutive(nums));
    System.out.println(longestConsecutive(nums2));
  }

  public static int longestConsecutive(int[] nums) {
    if (nums.length == 0) {
      return 0;
    }

    // Create a Set of the array
    Set<Integer> numSet = new HashSet<>();
    for (int num : nums) {
      numSet.add(num);
    }

    // At each sequence, continously check the set for num 1 more than the last number in the sequence
    // num is the start of a sequence when it does not have a left neighbor
    int result = 1;
    for (int num : nums) {
      int seqLength = 1;
      if (!numSet.contains(num - 1)) {
        while (numSet.contains(num + 1)) {
          seqLength++;
          num++;
        }
        result = Math.max(seqLength, result); //Set result to the larger of result and seqLength
      }
    }
    return result;
  }
}
