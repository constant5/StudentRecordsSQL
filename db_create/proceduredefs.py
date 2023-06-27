# SQL procedure definitions

PROCEDURES = {}

PROCEDURES['get_grades'] = '''
CREATE DEFINER=`admin`@`%` PROCEDURE `get_grades`(IN `sid` INT)
SELECT c.id, c.name, c.credits, g.grade
FROM students s
JOIN grades g
JOIN courses c
WHERE s.id = sid AND s.id=g.student_id and g.course_id = c.id
'''