export default function getStudentIdsSum(studentsList) {
  return studentsList.map((student) => student.id)
    .reduce((sum, currentStudentId) => sum + currentStudentId);
}
