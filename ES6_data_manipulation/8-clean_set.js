export default function cleanSet(set, startString) {
  const string = '';
  const sep = '';
  for (const ele of set.values()) {
    if (ele.startsWith(startString)) {
      string += sep + ele.slice(startString.length);
      sep = '-';
    }
  }
  return string;
}
