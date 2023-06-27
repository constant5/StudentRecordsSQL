from tabledefs import TABLES
from functiondefs import FUNCTIONS
from proceduredefs import PROCEDURES
import mysql.connector
from mysql.connector import errorcode
import logging

DB_NAME = 'studentrecords'

class DBCreator():
    def __init__(self, cnx) -> None:
        self.cnx = cnx
        self.cursor = cnx.cursor()
        self.__create_db__()
    
    def __create_db__(self):
            try:
                self.cursor.execute(f"USE {DB_NAME}")
                logging.info(f"Using DB {DB_NAME}")
            except mysql.connector.Error as err:
                logging.warning(f"Database {DB_NAME} does not exists.")
                if err.errno == errorcode.ER_BAD_DB_ERROR:
                    # create_database(cursor)
                    try:
                        self.cursor.execute(
                            f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
                        logging.info(f"Database {DB_NAME} created successfully.")
                    except mysql.connector.Error as err:
                        logging.error(f"Failed creating database: {err}")
                        exit(1)
                    self.cnx.database = DB_NAME
                else:
                    logging.error(err)
                    exit(1)


    def __def_db_objects__(self, sql_dict, type):
        for name in sql_dict:
            sql_description = sql_dict[name]
            try:
                logging.info(f"Creating {type} {name}: ")
                self.cursor.execute(sql_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    logging.warning(f"{name} already exists.")
                else:
                    logging.error(err.msg)
            else:
                logging.info("OK")

    def create_tables(self):
        self.__def_db_objects__(TABLES, type='table')
    
    def create_functions(self):
        self.__def_db_objects__(FUNCTIONS, type='function')
    
    def create_procedures(self):
        self.__def_db_objects__(PROCEDURES, type='procedure')

    def db_create(self):
        self.create_tables()
        self.create_functions()
        self.create_procedures()