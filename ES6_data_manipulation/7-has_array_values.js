export default function hasValuesFromArray(set, array) {
  // Iterate through each element in the array
  for (const element of array) {
    // Check if the element exists in the set
    if (!set.has(element)) {
      // If the element is not found in the set, return false
      return false;
    }
  }
  // If all elements were found in the set, return true
  return true;
}
