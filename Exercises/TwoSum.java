import java.util.HashMap;
import java.util.Map;

public class TwoSum {
  public static void main(String[] args) {
    int[] nums1 = {2,7,11,15};
    int target1 = 9;
    int[] nums2 = {3,2,4};
    int target2 = 6;
    int[] nums3 = {3,3};
    int target3 = 6;

    System.out.println(twoSum(nums1, target1)[0]);
    System.out.println(twoSum(nums1, target1)[1]);

    System.out.println(twoSum(nums2, target2)[0]);
    System.out.println(twoSum(nums2, target2)[1]);

    System.out.println(twoSum(nums3, target3)[0]);
    System.out.println(twoSum(nums3, target3)[1]);
  }

  //This approach does one pass over nums. While iterating and inserting elements into the hash table,
  //we are checking if the complement is in the hash table already. If so, return the indices.
  //Time complexity: O(n); traversing the list only once
  //Space complexity: O(n): The hash table stores at most n elements
  public static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (map.containsKey(complement)) {
        return new int[] {map.get(complement), i};
      }
      map.put(nums[i], i);
    }
    return null;
  }
}
