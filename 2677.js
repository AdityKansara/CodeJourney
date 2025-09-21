// #2677 - Chunk Array
// Problem solved by Adity
// Time Complexity: O(n) - Each element is visited once.
// Space Complexity: O(n) - A new array with the same total number of elements is created.

/**
 * Splits the input array into subarrays ("chunks") of a given size.
 *
 * @param {Array} arr - The input array to be chunked
 * @param {number} size - The size of each chunk
 * @return {Array} - An array containing subarrays (chunks) of the original array
 */
var chunk = function (arr, size) {
  const result = []; // Holds the final chunked array

  // Loop through the array, incrementing by 'size' each time
  for (let i = 0; i < arr.length; i += size) {
    // Slice from i to i + size (not including i + size) and push it into result
    result.push(arr.slice(i, i + size));
  }

  return result; // Return the array of chunks
};
