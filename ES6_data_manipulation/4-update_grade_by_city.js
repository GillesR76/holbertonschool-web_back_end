export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.city === city)
    .map((student) => {
      const studentsWithGrades = newGrades.find((getGrade) => getGrade.studentId === student.id);
      return {
        ...student,
        grade: studentsWithGrades ? studentsWithGrades.grade : 'N/A',
      };
    });
}
