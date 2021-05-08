#! /usr/bin/env python

import os
import sqlite3
import vars
import loger


class SqlDriver:
    
    def __init__(self, sql_db_file):
        self.__connect = sqlite3.connect(sql_db_file)
        self.__cursor = self.__connect.cursor()


    def exec_request(self, sqlRequest):
        self.__cursor.execute(sqlRequest)



    def exec_file(self, fname):
        request = self.__readf(fname)

        if request is not "":
            self.exec_request(request)

    def exec_files(self, files):
        for file in files:
            self.exec_file(file)


    def __readf(self, fname):
        if os.path.exists(fname) is not False:
            with open(fname, 'r') as file:
                return file.read()

        loger.write_log("ERROR:", "file not found: " + fname)
        return str("")