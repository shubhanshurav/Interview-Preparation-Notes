# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
	K = [[0 for x in range(W + 1)] for x in range(n + 1)]

	# Build table K[][] in bottom up manner
	for i in range(n + 1):
		for w in range(W + 1):
			## either row is 0 or column is 0
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1]
						+ K[i-1][w-wt[i-1]],
							K[i-1][w])
			else:
				## wt[i-1] > W
				## skip the current object
				## copy the value from the previous row
				K[i][w] = K[i-1][w]

	return K[n][W]


# Driver code
val = [1, 2, 3]
wt = [4, 5, 1]
W = 4
n = len(val)
## function calling
print("Maximum profit in 0-1 Knapsack is", knapSack(W, wt, val, n))
