export default function updateStudentGradeByCity(list, city, newGrades) {
  return list
    .filter((student) => student.location === city)
    .map((student) => {
      let grade = 'N/A'; // Default grade
      const gradeInfo = newGrades.find((gradeObj) => gradeObj.studentId === student.id);
      if (gradeInfo) {
        grade = gradeInfo.grade;
      }
      return {
        ...student,
        grade,
      };
    });
}
