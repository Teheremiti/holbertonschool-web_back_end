export default function getListStudentIds(studentsList) {
  if (!(studentsList instanceof Array)) {
    return [];
  }
return studentsList.map((student) => student.id);
}
