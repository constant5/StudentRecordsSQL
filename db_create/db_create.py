import sys
sys.path.append('.')
from dbcreator import DBCreator
from dbpopulate import BatchPopulator
import mysql.connector
import config
import logging
logging.basicConfig(level=logging.DEBUG)


if __name__=="__main__":
    cnx = mysql.connector.connect(user=config.username, 
                              password=config.password,
                              host=config.host,
                              port=config.port)
    
    # Create DB
    DBCreator(cnx).db_create()

    # Poplulate Database
    DBP = BatchPopulator(cnx, 
                    'data\\students.txt',
                    'data\\courses.txt',
                    'data\\grades.txt').insert_data()
    # test query
    cursor = cnx.cursor()
    query = ("SELECT f_name, m_name, l_name FROM students "
            "WHERE id = %s")
    cursor.execute(query, (1,))
    for (f_name, m_name, l_name) in cursor:
        print(f_name, m_name, l_name)
    cursor.close()
    cnx.close()
