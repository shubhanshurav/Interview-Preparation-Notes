/*
    ? Problem Statement: Find length of Longest Common Subsequence in a Dynamic Programming Memoized way.

    ! Time Complexity: O(m * n)
    ! Space Complexity: O(m * n)
*/

const dpMemoizedLCS = (string1: string, string2: string, position1: number, position2: number, memoizedMatrix: Array<Array<number>>): number => {
    // * Check if the function call has already been made & if the value has been memoized in the memoize matrix where m is the position of string1 and n is the position of string2. If there is a value we can directly return that only.
    if(memoizedMatrix[position1] && memoizedMatrix[position1][position2]) return memoizedMatrix[position1][position2];

    // * Here we check if any of the string has ended then we simply return 0 as no character is matched there.
    if(position1 > string1.length - 1 || position2 > string2.length - 1) return 0;

    // * We initiate a variable for the length of matching string from here on as 0.
    let currentLength = 0;

    // * Then we check the character is same at both the position, then can update the length of the maxMatchedLength by 1. Also call the the same function reccursively with position1 + 1 and position2 + 1 & add the result returned by it to the maxMatchedLength. Also set memoizedMatrix[position1][position2] to maxMatchedLength, making it as the max length that can be achieved by that combination.
    if(string1.charAt(position1) === string2.charAt(position2)){
        currentLength = 1 + dpMemoizedLCS(string1, string2, position1 + 1, position2 + 1, memoizedMatrix);

        memoizedMatrix[position1][position2] = currentLength;
    }
    // * If it is not the case, then we need to consider both the cases where we increase the position1 by 1 & then increase the position2 by 1. Now we need to to compare the result returned by both. Whichever is greater, we can simply take that into consideration and set maxMatchedLength as the that value. Also set memoizedMatrix[position1][position2] to maxMatchedLength, making it as the max length that can be achieved by that combination.
    else {
        currentLength = Math.max(dpMemoizedLCS(string1, string2, position1 + 1, position2, memoizedMatrix), dpMemoizedLCS(string1, string2, position1, position2 + 1, memoizedMatrix));

        memoizedMatrix[position1][position2] = currentLength;
    }

    // * Finally return the maxMatchedLength.
    return currentLength;
}

// * This function call the function dpMemoizedLCS with required params.
const getLCS = (string1: string, string2: string): number => {
    // * This is the main matrix to store the memoized values where we have m (length of string 1) number of rows & n (length of string 2) number of columns.
    let memoizedMatrix: Array<Array<number>> = [];

    for(let i=0; i<string1.length; i++) {
        memoizedMatrix.push(new Array(string2.length))
    }

    return dpMemoizedLCS(string1, string2, 0, 0, memoizedMatrix);
}

// ? Driver Code
console.log(getLCS("bd", "abcd"));