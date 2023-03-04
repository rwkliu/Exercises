public class PivotIndex {
  public static void main(String[] args) {
    int[] nums1 = {1,7,3,6,5,6};
    int[] nums2 = {1,2,3};
    int[] nums3 = {2,1,-1};

    System.out.println(pivotIndex(nums1));
    System.out.println(pivotIndex(nums2));
    System.out.println(pivotIndex(nums3));
  }

  public static int pivotIndex(int[] nums) {
    int leftsum = 0;
    int rightsum = 0;
    int total = 0;

    for (int i = 0; i < nums.length; i++) {
      total += nums[i];
    }

    for (int i = 0; i < nums.length; i++) {
      rightsum = total - leftsum - nums[i];
      if (leftsum == rightsum) {
        return i;
      }
      leftsum += nums[i];
    }
    return -1;
  }
}
