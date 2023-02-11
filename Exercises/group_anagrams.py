# Topic: Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 0:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 1:
# Input: strs = [""]
# Output: [[""]]
# Example 2:
# Input:  strs = ["a"]
# Output: [["a"]]

# Constraints
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
def is_anagram(output_array_str, str):
  #  if len != return false
  output_array_str_sorted = sorted(output_array_str)
  str_sorted = sorted(str)
  if (output_array_str_sorted == str_sorted):
    return True
  return False

def group_anagrams(string_array):
  #  check empty
  if len(string_array) == 0:
    return []
  output_array = []
  for element in string_array:
    add_flag = 0
    for sub_list in output_array:
      if(is_anagram(sub_list[0], element)):
        sub_list.append(element)
        add_flag = 1
    if add_flag == 0:
      new_sub_list = [element]
      output_array.append(new_sub_list)
    # print(output_array)

  return output_array

strs = ["eat","tea","tan","ate","nat","bat"]
strs2 = [""]
strs3 = ["a"]
print(group_anagrams(strs))
print(group_anagrams(strs2))
print(group_anagrams(strs3))