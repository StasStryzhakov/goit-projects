SELECT disciplines.name, students.fullname, round(avg(grades.grade), 2) AS a_grade
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
         LEFT JOIN disciplines ON disciplines.id = grades.discipline_id
WHERE disciplines.id = 1
GROUP BY students.id, disciplines.id
ORDER BY a_grade DESC LIMIT 1;