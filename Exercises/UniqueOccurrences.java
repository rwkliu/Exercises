import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.HashSet;

public class UniqueOccurrences {
  public static void main(String[] args) {
    int[] arr1 = {1,2,2,1,1,3};
    int[] arr2 = {1,2};

    System.out.println(uniqueOccurrences(arr1));
    System.out.println(uniqueOccurrences(arr2));
  }

  public static boolean uniqueOccurrences(int[] arr) {
    Map<Integer, Integer> occurrences = new HashMap<>();
    Set<Integer> numOccurrences = new HashSet<>();

    for (int element : arr) {
      if (occurrences.containsKey(element)) {
        occurrences.put(element, occurrences.get(element) + 1);
      } else {
        occurrences.put(element, 1);
      }
    }
    for (Integer o : occurrences.values()) {
      if (numOccurrences.contains(o)) {
          return false;
      }
      numOccurrences.add(o);
    }
    return true;
  }
}
