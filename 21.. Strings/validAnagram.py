# Problem: Valid Anagram (LeetCode #242)
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.
# An anagram uses exactly the same characters the same number of times.

# Approach: Character Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(1)  — at most 26 distinct lowercase letters

def isAnagram(s, t):
    # strings of different lengths cannot be anagrams
    if len(s) != len(t):
        return False

    # count character frequencies in s and t simultaneously
    count = {}
    for ch_s, ch_t in zip(s, t):
        count[ch_s] = count.get(ch_s, 0) + 1
        count[ch_t] = count.get(ch_t, 0) - 1

    # all counts should cancel out to zero for a valid anagram
    return all(v == 0 for v in count.values())


# driver code
print(isAnagram("anagram", "nagaram"))  # Output: True
print(isAnagram("rat", "car"))          # Output: False
