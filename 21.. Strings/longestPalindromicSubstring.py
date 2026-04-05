# Problem: Longest Palindromic Substring (LeetCode #5)
# Given a string s, return the longest palindromic substring in s.

# Approach: Expand Around Center
# For each character (and each pair of adjacent characters), expand outward
# as long as the characters on both sides match.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def longestPalindrome(s):
    def expandAroundCenter(left, right):
        # expand while within bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return the palindrome substring found
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # odd-length palindromes (single character center)
        odd = expandAroundCenter(i, i)
        # even-length palindromes (two character center)
        even = expandAroundCenter(i, i + 1)

        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even

    return longest


# driver code
print(longestPalindrome("babad"))   # Output: "bab" (or "aba")
print(longestPalindrome("cbbd"))    # Output: "bb"
print(longestPalindrome("racecar")) # Output: "racecar"
