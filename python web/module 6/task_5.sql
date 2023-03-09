SELECT teachers.fullname, disciplines.name
FROM teachers
         LEFT JOIN disciplines ON disciplines.teacher_id = teachers.id
WHERE teachers.id = 1;