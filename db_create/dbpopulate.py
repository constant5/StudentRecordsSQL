import logging


def commit(func):
    def inner(*args, **kwargs):
        c, e = func(*args, **kwargs)
        logging.debug((c,e))
        args[0].cursor.execute(c,e)
        args[0].cnx.commit()
        return
    return inner


class DBPopulate():
    def __init__(self,cnx) -> None:
        self.cnx = cnx
        self.cursor = self.cnx.cursor()

    @commit
    def __add_student__(self, f_name, l_name, m_name=None):
        add_student = ("INSERT into `students`"
                       "(f_name, m_name, l_name)"
                       "VALUES(%s, %s, %s)")
        return add_student, (f_name, m_name, l_name)
        
    @commit
    def __add_course__(self, cid, name, credits):
        add_course = ("INSERT into `courses`"
                      "(id, name, credits)"
                      "VALUES(%s, %s, %s)")
        return add_course, (cid, name, credits)
    
    @commit
    def __add_grade__(self, sid, cid, grade):
        add_grade = ("INSERT into `grades`"
                     "(student_id, course_id, grade)"
                     "VALUES(%s, %s, %s)")
        return add_grade, (sid, cid, grade)

    def __del__(self):
        pass

class BatchPopulator(DBPopulate):
    def __init__(self, cnx, student_file, course_file, grades_file):
        super().__init__(cnx)
        self.student_file = student_file
        self.course_file = course_file
        self.grades_file = grades_file
    
    def batch_students(self):
        with open(self.student_file) as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                if not line2: break
                id = int(line1)
                name = str(line2).strip('\n').split(' ')
                if len(name) ==3:
                    f_name, m_name, l_name =  name
                else: 
                    f_name, l_name = name
                    m_name = None
                self.__add_student__(f_name, l_name, m_name)
    
    def batch_courses(self):
        with open (self.course_file) as f:
            while True:
                line1 = f.readline()
                line2 = f.readline()
                line3 = f.readline()
                if not line3: break
                id = int(line1)
                name = str(line2).strip('\n')
                credits = int(line3)
                self.__add_course__(id, name, credits)
    
    def batch_grades(self):
        with open (self.grades_file) as f:
            while True:
                    line1 = f.readline()
                    line2 = f.readline()
                    line3 = f.readline()
                    if not line3: break
                    sid = int(line1)
                    cid = int(line2)
                    grd = str(line3).strip('\n')
                    self.__add_grade__(sid,cid,grd)

    def insert_data(self):
        self.batch_students()
        self.batch_courses()
        self.batch_grades()


    
