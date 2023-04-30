/*
    ? Problem Statement: Q2 of Assignment sheet.
    ? Solution Creator: Ankan Bhattacharya.

    ! Time Complexity: O(n)
    ! Space Complexity: O(1)
    ! Algo used: Counting Sort
*/

// * Here we are implementing counting sort as we know that we have only three numbers: 0, 1 and 2. Here we first count how many numbers of 0, 1 and 2 are there in the array. Then we simply replace the numbers in position by first placing 0 followed by 1 and 2. This facilitates us to do the sorting in O(n) time and with constant extra space.
const countingSort = (nums: Array<number>): void  => {
    let zeroCount = 0;
    let oneCount = 0;
    let twoCount= 0;

    // * Counting number of zeros, ones and twos.
    for(let num of nums) {
        if(num === 0) zeroCount++;
        else if(num === 1) oneCount++;
        else if(num === 2) twoCount++;
    }

    let currentPosition = 0;

    // * Putting zeros in its correct places.
    while(zeroCount > 0 && currentPosition < nums.length){
        nums[currentPosition] = 0;
        zeroCount--;
        currentPosition++;
    }

    // * Putting ones in its correct places.
    while(oneCount > 0 && currentPosition < nums.length){
        nums[currentPosition] = 1;
        oneCount--;
        currentPosition++;
    }

    // * Putting two in its correct places.
    while(twoCount > 0 && currentPosition < nums.length){
        nums[currentPosition] = 2;
        twoCount--;
        currentPosition++;
    }
}


const sortColors = (nums: Array<number>): void => {
    countingSort(nums);
}


// ? Driver Code.
const nums = [2,0,2,1,1,0];
sortColors(nums);
console.log(nums);
