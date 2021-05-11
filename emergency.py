#! /usr/bin/env python

import sqliteDriver as sql
from vars import *


class Emergency:

    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/emergency.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )
        self.__sqlDriver.exec_file(
            "{SQL_SCRIPOTS_DIR_PATH}/emergency.txt".format(
                SQL_SCRIPOTS_DIR_PATH=SQL_SCRIPOTS_DIR_PATH
            )
        )



    def insert(self,
            id_object,
            first_name,
            last_name,
            middle_name,
            type_of_emergency,    
            ponumber_of_victims):

            req = """
                INSERT INTO Emergency
                (id_object, first_name, last_name, middle_name, type_of_emergency, ponumber_of_victims)
                VALUES
                ('{id_object}', '{first_name}', '{last_name}', '{middle_name}', '{type_of_emergency}', '{ponumber_of_victims}');
            """.format(
                id_object=id_object,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                type_of_emergency=type_of_emergency,
                ponumber_of_victims=ponumber_of_victims
            )

            self.__sqlDriver.exec_request(req) 