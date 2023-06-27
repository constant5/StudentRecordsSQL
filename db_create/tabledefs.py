# table definitions

TABLES = {}

TABLES['students'] = (
    "CREATE TABLE `students`("
    "id int(11) NOT NULL AUTO_INCREMENT,"
    "f_name varchar(20) NOT Null,"
    "m_name varchar(20),"
    "l_name varchar(20) NOT Null,"
    "PRIMARY KEY (id),"
    "KEY (l_name)"
    ") ENGINE= InnoDB")

TABLES['courses'] = (
    "CREATE TABLE `courses`("
    "id int(6) NOT NULL,"
    "name varchar(20),"
    "credits int(1) NOT NULL,"
    "PRIMARY KEY (id)"
    ") ENGINE= InnoDB") 

TABLES['grades'] = (
    "CREATE TABLE `grades`("
    "id int NOT NULL AUTO_INCREMENT,"
    "student_id int(6) NOT NULL,"
    "course_id int(6) NOT NULL,"
    "grade varchar(1) NOT NULL,"
    "PRIMARY KEY(id),"
    "CONSTRAINT student_id_fk FOREIGN KEY (`student_id`)"
        "REFERENCES `students`(`id`) ON DELETE CASCADE,"
    "CONSTRAINT `course_id_fk` FOREIGN KEY (`course_id`)"
        "REFERENCES `courses`(`id`) ON DELETE CASCADE" 
    ") ENGINE = InnoDB")
