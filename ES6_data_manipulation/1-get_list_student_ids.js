export default function getListStudentIds(list) {
  // Check if the input is an array
  if (!Array.isArray(list)) {
    return [];
  }

  // extract the id property from each object
  return list.map((item) => item.id);
}
