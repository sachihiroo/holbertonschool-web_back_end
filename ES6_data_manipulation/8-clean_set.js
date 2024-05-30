export default function cleanSet(set, startString) {
  // Check if startString is empty
  if (startString === '') return '';

  // Filter and map the set to get the substrings after startString
  const substrings = Array.from(set)
    .filter((value) => typeof value === 'string' && value.startsWith(startString))
    .map((value) => value.substring(startString.length).trim());

  // Join the substrings with a dash
  return substrings.join('-');
}
