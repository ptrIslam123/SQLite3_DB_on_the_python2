#! /usr/bin/env python

import sqliteDriver as sql
from vars import *


class Employees:

    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/employees.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )
        self.__sqlDriver.exec_file(
            "{SQL_SCRIPOTS_DIR_PATH}/employees.txt".format(
                SQL_SCRIPOTS_DIR_PATH=SQL_SCRIPOTS_DIR_PATH
            )
        )


    def insert(self,
            id_employee,
            first_name,
            last_name,
            middle_name,
            gender,   
            post):
        
        req = """
            INSERT INTO Employees
            (id_employee, first_name, last_name, middle_name, gender, post)
            VALUES
            ('{id_employee}', '{first_name}', '{last_name}', '{middle_name}', '{gender}', '{post}');
        """.format(
            id_employee=id_employee,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            gender=gender,
            post=post
        )

        self.__sqlDriver.exec_request(
            req
        )



    def update_by_id(self, 
                id_employee,
                first_name,
                last_name,
                middle_name,
                gender,   
                post):
        req = """
            UPDATE Employees
            SET
            first_name='{first_name}',
            last_name='{last_name}',
            middle_name='{middle_name}',
            gender='{gender}',
            post='{post}'
            WHERE id_employee='{id_employee}';
        """.format(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            gender=gender,
            post=post,
            id_employee=id_employee
        )

        self.__sqlDriver.exec_request(
            req
        )


    def remove_by_id(self, id_employee):
        req = """
            DELETE FROM Employees
            WHERE id_employee='{id_employee}'
        """.format(
            id_employee=id_employee
        )

        self.__sqlDriver.exec_request(
            req
        )

    

    def select_by_id(self, id_employee):
        req = """
            SELECT *
            FROM Employees
            WHERE id_employee='{id_employee}';
        """.format(id_employee=id_employee)

        self.__sqlDriver.exec_request(
            req
        )

        return self.__sqlDriver.fetchone()


    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Employees;
            """
        )

        return self.__sqlDriver.fetchall()

    
