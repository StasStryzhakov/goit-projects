SELECT teachers.fullname, round(avg(grades.grade), 2) AS a_grade
FROM grades
         LEFT JOIN disciplines ON disciplines.id = grades.discipline_id
         LEFT JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE teachers.id = 1
GROUP BY teachers.fullname;