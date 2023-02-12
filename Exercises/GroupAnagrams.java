import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class GroupAnagrams {
  public static void main(String[] args) {
    String[] strs1 = {"eat","tea","tan","ate","nat","bat"};
    String[] strs2 = {""};
    String[] strs3 = {"a"};
    System.out.println(groupAnagrams(strs1));
    System.out.println(groupAnagrams(strs2));
    System.out.println(groupAnagrams(strs3));
  }

  public static boolean isEqualStrings(char[] str1, char[] str2) {
    if (str1.length != str2.length) {
      return false;
    }
    for (int i = 0; i < str1.length; i++) {
      if (str1[i] != str2[i]) {
        return false;
      }
    }
    return true;
  }

  public static boolean isAnagram(String subListElement, String str) {
    char[] sortedSubListElement = subListElement.toCharArray();
    Arrays.sort(sortedSubListElement);
    char[] sortedStr = str.toCharArray();
    Arrays.sort(sortedStr);

    if (isEqualStrings(sortedSubListElement, sortedStr)) { 
      return true;
    }
    return false;
  }

  public static List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> output = new ArrayList<>();
    List<String> firstList = new ArrayList<>(Arrays.asList(strs[0]));
    output.add(firstList);
    
    if (strs.length == 0) {
      return output;
    }

    for (int i = 1; i < strs.length; i++) {
      String element = new String(strs[i]);
      boolean addFlag = false;

      for (int j = 0; j < output.size(); j++) {
        List<String> subList = new ArrayList<>(output.get(j));
        if (isAnagram(subList.get(0), element)) {
          output.get(j).add(element);
          addFlag = true;
        }
      }
      if (addFlag == false) {
        List<String> newSubList = new ArrayList<>(Arrays.asList(element));
        output.add(newSubList);
      }
    }
    return output;
  }
}
