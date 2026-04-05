# Problem: Two Sum (LeetCode #1)
# Given an array of integers nums and an integer target,
# return indices of the two numbers that add up to target.
# You may assume exactly one solution exists.

# Approach: Hash Map (one-pass)
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    # map each number to its index as we iterate
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        # if complement already seen, we found our pair
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# driver code
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))   # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2)) # Output: [1, 2]
