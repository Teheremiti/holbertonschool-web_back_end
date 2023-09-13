/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    const newArr = []
    for (const ele of array) {
        newArr.push(appendString + ele);
    }

    return newArr;
}
