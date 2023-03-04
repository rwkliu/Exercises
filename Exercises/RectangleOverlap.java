class RectangleOverlap {
  public static void main(String[] args) {
    //true
    int[] rec1_1 = {0,0,2,2};
    int[] rec2_1 = {1,1,3,3};
    
    //false
    int[] rec1_2 = {0,0,1,1};
    int[] rec2_2 = {1,0,2,1};
    
    //false
    int[] rec1_3 = {0,0,1,1};
    int[] rec2_3 = {2,2,3,3};

    System.out.println(isRectangleOverlap(rec1_1, rec2_1));
    System.out.println(isRectangleOverlap(rec1_2, rec2_2));
    System.out.println(isRectangleOverlap(rec1_3, rec2_3));
  }

  /*
   * Two rectangles overlap if the area of their intersection is positive. 
   * Two rectangles that only touch at the corner or edges do not overlap.
   * The main idea of the solution is that the intersection area is positive. Therefore, the width
   * and height of the intersection should both be positive. The width is positive when the smaller
   * of the smallest of the largest x-coordinates is larger than the largest of the smallest x-coordinates.
   * The height is similar.
   */
  public static boolean isRectangleOverlap(int[] rec1, int[] rec2) {
    return (Math.min(rec1[2], rec2[2]) > Math.max(rec1[0], rec2[0])) &&
            Math.min(rec1[3], rec2[3]) > Math.max(rec1[1], rec2[1]);
  }
}
