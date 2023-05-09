# This is the memoization approach of
# 0 / 1 Knapsack in Python in simple
# we can say recursion + memoization = DP


## Method definition
# We initialize the matrix with -1 at first.
def knapsack(wt, val, W, n):
	t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
	# base conditions
	if n == 0 or W == 0:
		return 0

	# memoization approach is helpful
	# avoiding the problem of overlapping subproblems	
	if t[n][W] != -1:
		return t[n][W]

	# two choices: Max(either we can skip the object or we can include the object)
	if wt[n-1] <= W:
		t[n][W] = max(
			# including the object
			# recursion
			val[n-1] + knapsack(
				wt, val, W-wt[n-1], n-1),
			# skipping the object
			# recursion
			knapsack(wt, val, W, n-1))

		return t[n][W]

	elif wt[n-1] > W:
		# skip the object completely
		t[n][W] = knapsack(wt, val, W, n-1)
		return t[n][W]


# driver code
# val is profit array
# W is the maximum capacity
val = [60, 100, 120 ]
wt = [10, 20, 30 ]
W = 50
n = len(val)
print(knapsack(wt, val, W, n))