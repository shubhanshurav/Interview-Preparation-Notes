# Problem: Group Anagrams (LeetCode #49)
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

# Approach: Sort each word as a key for grouping
# Time Complexity: O(n * k log k)  — n strings, k is max string length
# Space Complexity: O(n * k)

def groupAnagrams(strs):
    anagram_map = {}

    for word in strs:
        # sort the word to get a canonical key shared by all its anagrams
        key = tuple(sorted(word))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(word)

    return list(anagram_map.values())


# driver code
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
# Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

strs2 = [""]
print(groupAnagrams(strs2))  # Output: [[""]]

strs3 = ["a"]
print(groupAnagrams(strs3))  # Output: [["a"]]
