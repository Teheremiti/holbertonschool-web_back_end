export default function appendToEachArrayValue(array, appendString) {
    for (const ele of array) {
        ele = appendString + ele;
    }

    return array;
}
