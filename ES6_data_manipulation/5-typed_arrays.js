export default function createInt8TypedArray(length, position, value) {
  // Check if the position is within the valid range
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer with the specified length
  const buffer = new ArrayBuffer(length);

  // Create a DataView to manipulate the buffer
  const view = new DataView(buffer);

  // Set the value at the specified position in the DataView
  view.setInt8(position, value);

  // Return the DataView
  return view;
}
