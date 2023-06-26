from db_create.tabledefs import TABLES, DB_NAME
from db_create.dbpopulate import BatchPopulator
import mysql.connector
from mysql.connector import errorcode
import config
import logging
logging.basicConfig(level=logging.DEBUG)

cnx = mysql.connector.connect(user=config.username, 
                              password=config.password,
                              host=config.host,
                              port=config.port)
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        logging.error("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    logging.info("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        logging.info("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        logging.error(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        logging.info("Creating table {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            logging.info("already exists.")
        else:
            logging.error(err.msg)
    else:
        logging.info("OK")


# DBP = BatchPopulator(cnx, 
#                 'data\\students.txt',
#                 'data\\courses.txt',
#                 'data\\grades.txt').insert_data()


query = ("SELECT f_name, m_name, l_name FROM students "
         "WHERE id = %s")
cursor.execute(query, (1,))
for (f_name, m_name, l_name) in cursor:
    print(f_name, m_name, l_name)

cnx.close()
