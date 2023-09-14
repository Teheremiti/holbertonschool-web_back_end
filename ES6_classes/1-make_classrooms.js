/* eslint-disable */
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
    class1 = new ClassRoom(19);
    class2 = new ClassRoom(20);
    class3 = new ClassRoom(34);
    return [class1, class2, class3];
}
