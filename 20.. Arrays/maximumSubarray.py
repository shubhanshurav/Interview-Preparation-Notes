# Problem: Maximum Subarray (LeetCode #53)
# Given an integer array nums, find the subarray with the largest sum
# and return its sum.

# Approach: Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

def maxSubArray(nums):
    # start with the first element as both the current and max sum
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        # either extend the existing subarray or start a new one from current element
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# driver code
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))   # Output: 6  (subarray [4, -1, 2, 1])

nums2 = [1]
print(maxSubArray(nums2))  # Output: 1

nums3 = [5, 4, -1, 7, 8]
print(maxSubArray(nums3))  # Output: 23
