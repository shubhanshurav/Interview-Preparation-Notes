/*
    ? Problem Statement: Q1 of Assignment 8.
    ? Solution Creator: Ankan Bhattacharya.

    ! Time Complexity:
     ! - Worst Case = O(n^2)
     ! - Average and Best Case = Theta(n)
    
    ! Space Complexity: O(1)

    ? Note: We are using a recursive call here so it would automatically take O(log n) space to store the function calls in a stack.
*/

const partition = (nums: Array<number>, lb: number, ub: number): number => {
    // *fixing the pivot
    let pivot = nums[lb];

    // *lower portion segmenting pointer
    let i = lb;
    
    for(let j=i+1; j<=ub; j++){
        // *If value at j-th position is less than or equal to pivot, then first increment i by 1 and swap the values at i and j
        if(nums[j] <= pivot) {
            i++;
            [nums[i], nums[j]] = [nums[j], nums[i]];
        }
    }

    // *Now we swap the i-th index with lower bound. Now finally pivot's value has been placed at its correct index
    [nums[lb], nums[i]] = [nums[i], nums[lb]];

    // *Let's return the pivot's correct index
    return i;
};

// *This function is reposnible for finding the k-th smallest term. If the Kth smallest Index is greater than the length f the array then it returns the highest index of the sorted array.
const getKSmallest = (nums: Array<number>, kSmallestIndex: number, lb: number, ub: number): number => {
    if(lb === ub && lb === (kSmallestIndex - 1)) return nums[lb];
    if (lb < ub) {
        const pivot = partition(nums, lb, ub);
        const requiredIndex = kSmallestIndex - 1;

        // *If the pivot returned i.e. the index that has been put in its correct place is returned is equivalent to k-th smallest term we return the number at that particular index.
        if(pivot === requiredIndex) return nums[kSmallestIndex - 1];

        // *If the pivot returned is actually less than that of the required smallest index then we need to search the larger side & we need to only call for pivot + 1 to upper bound.
        if(pivot < requiredIndex) return getKSmallest(nums, kSmallestIndex, pivot + 1, ub);

        // *Else we know that the pivot is greater than that of he required smallest index, then we need to search the smaller side & we need to only call for lower bound upto pivot - 1.
        else return getKSmallest(nums, kSmallestIndex, lb, pivot - 1);
    }

    return nums[nums.length - 1];
};

// ? Driver Code
const nums = [40, 25, 68, 79, 52, 66, 89, 97];
console.log(getKSmallest(nums, 2, 0, nums.length - 1));
console.log(getKSmallest(nums, 3, 0, nums.length - 1));

const nums2 = [7, 10, 4, 3, 20, 15];
console.log(getKSmallest(nums2, 3, 0, nums.length - 1));
console.log(getKSmallest(nums2, 4, 0, nums.length - 1));