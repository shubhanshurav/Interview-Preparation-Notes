# Python code to implement the
# matrix chain multiplication using recursion

import sys

# Matrix A[i] has dimension p[i-1] x p[i]
# for i = 1..n
def MatrixChainOrder(p, i, j):
	## base case condition
	if i == j:
		return 0

	minVal = sys.maxsize

	# Place parenthesis at different places
	# between first and last matrix,
	# recursively calculate count of multiplications
	# for each parenthesis placement
	# and return the minimum count
	for k in range(i, j):

		## recursive call
		count = (MatrixChainOrder(p, i, k)
				+ MatrixChainOrder(p, k + 1, j)
				+ p[i-1] * p[k] * p[j])

		if count < minVal:
			minVal = count

	# Return minimum count
	return minVal


# Driver code
if __name__ == '__main__':
	arr = [1, 3, 1, 2, 3]
	N = len(arr)
	
	# Function call
	print("Minimum number of multiplications is ", MatrixChainOrder(arr, 1, N-1))


