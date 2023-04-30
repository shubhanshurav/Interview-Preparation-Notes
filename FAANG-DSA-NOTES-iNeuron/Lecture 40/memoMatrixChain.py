# Python program using memoization
import sys
dp = [[-1 for i in range(100)] for j in range(100)]

# Function for matrix chain multiplication
def matrixChainMemoised(p, i, j):
	## base case condition
	if(i == j):
		return 0
	
	## already solved that subproblem
	if(dp[i][j] != -1):
		return dp[i][j]
	
	dp[i][j] = sys.maxsize
	
	for k in range(i,j):
		## recursion call 
		dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) + matrixChainMemoised(p, k + 1, j)+ p[i - 1] * p[k] * p[j])
	
	return dp[i][j]

def MatrixChainOrder(p,n):
	i = 1
	j = n - 1
	return matrixChainMemoised(p, i, j)

# Driver Code
arr = [1, 3, 1, 2, 3]
n = len(arr)
print("Minimum number of multiplications is",MatrixChainOrder(arr, n))

