#! /usr/bin/env python

import sqliteDriver as sql
from vars import *
import loger



    

def main():
    cursor = sql.SqlDriver(SQL_DB_DIR_PATH + "main.db")
    cursor.exec_files([
        SQL_SCRIPOTS_DIR_PATH + "attemdants.txt", 
        SQL_SCRIPOTS_DIR_PATH + "emergency.txt", 
        SQL_SCRIPOTS_DIR_PATH + "employees.txt", 
        SQL_SCRIPOTS_DIR_PATH + "monitoring_eenter_of_emergency.txt",
        SQL_SCRIPOTS_DIR_PATH + "test2.txt"
    ])




if __name__ == "__main__":
    main()
