export default function getStudentIdsSum(studentsList) {
  return studentsList.reduce((sum, currentStudent) => sum + currentStudent.id);
}
