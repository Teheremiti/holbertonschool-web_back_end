/* eslint-disable */
export default function cleanSet(set, startString) {
  if (!startString || !(startString instanceof String)) {
    return '';
  }

  const string = '';
  const sep = '';
  for (const ele of set.values()) {
    if (ele && ele.startsWith(startString)) {
      string += `${sep}${ele.slice(startString.length)}`;
      sep = '-';
    }
  }
  return string;
}
