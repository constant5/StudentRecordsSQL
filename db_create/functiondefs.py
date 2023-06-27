# SQL function definitions

FUNCTIONS = {}

FUNCTIONS['convert_grade'] = '''
CREATE DEFINER=`admin`@`%` FUNCTION `convert_grade`(`letter_grade` VARCHAR(1)) RETURNS decimal(2,1) unsigned
    DETERMINISTIC
RETURN 
    CASE 
        WHEN letter_grade='A' THEN 4.0
        WHEN letter_grade='B' THEN 3.0
        WHEN letter_grade='C' THEN 2.0
        WHEN letter_grade='D' THEN 1.0
    ELSE 0.0
    END
'''

FUNCTIONS['get_gpa'] = '''
CREATE DEFINER=`admin`@`%` FUNCTION `get_gpa`(`sid` INT) RETURNS decimal(3,2) unsigned
    DETERMINISTIC
RETURN(
SELECT sum(convert_grade(g.grade)*c.credits)/sum(c.credits) FROM `students` s
JOIN `grades` g
JOIN `courses` c
WHERE g.student_id = s.id AND s.id = sid AND g.course_id=c.id)
;'''