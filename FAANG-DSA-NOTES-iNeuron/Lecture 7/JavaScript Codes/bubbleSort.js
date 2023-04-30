
function bubbleSort(array) {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length - i - 1; j++) {
      if (array[j + 1] < array[j]) {
        [array[j + 1], array[j]] = [array[j], array[j + 1]];
      }
    }
  }
  return array;
}

console.log(bubbleSort([2, 34, 56, 1, 25, 89, 10, 65]))