/* eslint-disable */
export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList.filter((student) => student.location === city)
    .map((student) => {
      for (const newGrade of newGrades) {
        let finalGrade = 'N/A'
        if (student.id === newGrade.studentId) {
          finalGrade = newGrade.grade;
        }
        const studentUpdate = { ...student };
        studentUpdate.grade = finalGrade;
      }
    });
}
