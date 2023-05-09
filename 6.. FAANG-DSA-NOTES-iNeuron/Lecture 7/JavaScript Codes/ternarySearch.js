
function ternarySearch(left, right, target, arr){
	//If the right side of array is smaller than the left, then the element doesn't exist in the array 
	if (right >= left)
	{
		//Find the two mid points to divide the array into three parts
		let mid1 = Math.floor(left + (right - left) /3);
		let mid2 = Math.floor(right - (right - left) /3);

		//We check both the mid point to see if it is the target element
		if (arr[mid1] == target) {
			return mid1;
		}
		else if (arr[mid2] == target) {
			return mid2;
		}

		//First part of the array
		if (target < arr[mid1]) {
			return ternarySearch(left, mid1 - 1, target, arr);
		}	//Third part of the array
		else if (target > arr[mid2]) {
			return ternarySearch(mid2 + 1, right, target, arr);
		}	//Second part of the array
		else {
			return ternarySearch(mid1 + 1, mid2 - 1, target, arr);
		}
	}
	return -1;
}

console.log(ternarySearch(0, 7, 65, [1, 2, 10, 25, 34, 56, 65, 89]))