# Problem: Product of Array Except Self (LeetCode #238)
# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all elements of nums except nums[i].
# Solve it without using division and in O(n) time.

# Approach: Prefix and Suffix Products
# Time Complexity: O(n)
# Space Complexity: O(1) — output array not counted as extra space

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # forward pass: result[i] holds product of all elements to the LEFT of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # backward pass: multiply by product of all elements to the RIGHT of i
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# driver code
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))   # Output: [24, 12, 8, 6]

nums2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
