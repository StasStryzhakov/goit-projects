SELECT students.fullname, ROUND(AVG(grades.grade), 2) AS a_grade
FROM grades
         LEFT JOIN students ON students.id = grades.student_id
GROUP BY students.id
ORDER BY a_grade DESC LIMIT 5;