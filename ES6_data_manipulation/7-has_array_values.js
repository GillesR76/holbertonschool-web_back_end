export default function hasValuesFromArray(set, array) {
  return array.every((val) => set.has(val));
}
