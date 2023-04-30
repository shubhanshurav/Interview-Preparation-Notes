# Dynamic Programming implementation of LCS problem
# Approach - Tabulation
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

# Task - To print the string of longest common subsequence
def lcs(X , Y):
	# find the length of the strings
	# m - number of rows
	# n - number of columns
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	LCS_table = [[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			## base condition
			if i == 0 or j == 0 :
				LCS_table[i][j] = 0
			## if there is a match of characters in string1 and string2
			elif X[i-1] == Y[j-1]:
				LCS_table[i][j] = 1 + LCS_table[i-1][j-1]
			else:
			## if there is no match of characters in string1 and string2
				LCS_table[i][j] = max(LCS_table[i-1][j] , LCS_table[i][j-1])

	return LCS_table[m][n]


# Driver code
string1 = "AGGTAB"
string2 = "GXTXAYB"
## output string - "GTAB"
## function calling
print ("Length of LCS is ", lcs(string1, string2) )


