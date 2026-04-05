# Problem: Merge Intervals (LeetCode #56)
# Given an array of intervals, merge all overlapping intervals and
# return an array of the non-overlapping intervals that cover all input intervals.

# Approach: Sort then Merge
# Time Complexity: O(n log n)  — dominated by sorting
# Space Complexity: O(n)

def merge(intervals):
    # sort intervals by their start value
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            # overlapping: extend the last merged interval if needed
            merged[-1][1] = max(last_end, end)
        else:
            # no overlap: add as a new interval
            merged.append([start, end])

    return merged


# driver code
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))   # Output: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1, 4], [4, 5]]
print(merge(intervals2))  # Output: [[1, 5]]
