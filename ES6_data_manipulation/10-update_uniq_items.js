export default function updateUniqueItems(map) {
  // Check if the argument is a Map
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate over the map entries and update quantities
  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });

  return map;
}
