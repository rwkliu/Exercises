import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

//Time Complexity: O(NKlogK), where N is the length of strs, and K is the max length of a string in
//strs. The outer loop is O(N) because we're iterating through each string, and sorting each string
//is O(KlogK) time.
//Space Complexity: O(NK), the total amount of information stored in output

class GroupAnagrams {                                                                               
  public static void main(String[] args) {                                                          
    String[] strs1 = {"eat","tea","tan","ate","nat","bat"};                                         
    String[] strs2 = {""};                                                                          
    String[] strs3 = {"a"};                                                                         
    System.out.println(groupAnagrams(strs1));                                                       
    System.out.println(groupAnagrams(strs2));                                                       
    System.out.println(groupAnagrams(strs3));                                                       
  }                                                                                                 

  //Maintain a map where each key is a sorted string and its values are a list of words in str
  //that are anagrams of the key                                                                    
  public static List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> output = new ArrayList<>();
    if (strs.length == 0) {
      return output;
    }
    Map<String, List<String>> anagrams = new HashMap<>();
   //Go through each string in the input array and check if the string is anagram of any keys in the 
   //hash map. Add string to key. Otherwise, add current string's sorted string and current string
   //as a new key,value pair to the hash map
    for(String str : strs) {
      char[] sortedStr = str.toCharArray();
      Arrays.sort(sortedStr);
      String key = String.valueOf(sortedStr);
      if (anagrams.containsKey(key) == false) {
        List<String> newsubList = new ArrayList<>();
        anagrams.put(key, newsubList);
      }
      anagrams.get(key).add(str);
    }
    for (Map.Entry<String, List<String>> anagramList : anagrams.entrySet()) {
      output.add(anagramList.getValue());
    }

    return output;
  }
} 
