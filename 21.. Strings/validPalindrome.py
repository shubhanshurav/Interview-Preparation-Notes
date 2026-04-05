# Problem: Valid Palindrome (LeetCode #125)
# A phrase is a palindrome if, after converting all uppercase letters to lowercase
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Return true if s is a palindrome, or false otherwise.

# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def isPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # skip non-alphanumeric characters from both ends
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # compare characters in a case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# driver code
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))                      # Output: False
print(isPalindrome(" "))                               # Output: True
