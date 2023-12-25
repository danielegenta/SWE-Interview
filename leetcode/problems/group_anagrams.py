'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from ast import List
from collections import defaultdict

# complexity
# time: o(n * m)

def groupAnagrams(strs):
    result = defaultdict(list) # haspmap initialized with empty list []
    for s in strs:
        char_map = [0] * 26 # represents chars a...z (key)
        for c in s:
            char_map[ord(c) - ord('a')] += 1
        result[tuple(char_map)].append(s)
    return result.values()
        
# example
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))