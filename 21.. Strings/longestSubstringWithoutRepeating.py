# Problem: Longest Substring Without Repeating Characters (LeetCode #3)
# Given a string s, find the length of the longest substring
# that contains no repeating characters.

# Approach: Sliding Window with Hash Map
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))  — m is the size of the character set

def lengthOfLongestSubstring(s):
    # map each character to its most recent index
    char_index = {}
    max_length = 0
    left = 0  # left boundary of the sliding window

    for right, char in enumerate(s):
        # if character already in window, move left boundary past its last occurrence
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        # update the last seen index of this character
        char_index[char] = right
        # update the max window size
        max_length = max(max_length, right - left + 1)

    return max_length


# driver code
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3  ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1  ("b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3  ("wke")
