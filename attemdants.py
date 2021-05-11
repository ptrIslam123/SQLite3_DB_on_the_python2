#! /usr/bin/env python

import sqliteDriver as sql
from vars import *

class Attemdants:

    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/attemdants.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )
        self.__sqlDriver.exec_file(
            "{SQL_SCRIPOTS_DIR_PATH}/attemdants.txt".format(
                SQL_SCRIPOTS_DIR_PATH=SQL_SCRIPOTS_DIR_PATH
            )
        )



    def insert(self,
            id_attemdant,
            first_name,
            last_name,
            middle_name,
            start_of_shift,
            end_of_shift):


            req = """INSERT INTO Attemdants
                    (id_attemdant, first_name, last_name, middle_name, start_of_shift, end_of_shift)
                    VALUES 
                    ('{id_attemdant}', '{first_name}', '{last_name}', '{middle_name}', '{start_of_shift}', '{end_of_shift}');""".format(
                        id_attemdant=id_attemdant, 
                        first_name=first_name, 
                        last_name=last_name, 
                        middle_name=middle_name, 
                        start_of_shift=start_of_shift, 
                        end_of_shift=end_of_shift
                    )
                    
            self.__sqlDriver.exec_request(
                req
            )



    def update_by_id(self,
                id_attemdant,
                first_name,
                last_name,
                middle_name,
                start_of_shift,
                end_of_shift):

                req = """
                    UPDATE Attemdants
                    SET
                    first_name='{first_name}',
                    last_name='{last_name}',
                    middle_name='{middle_name}',
                    start_of_shift='{start_of_shift}',
                    end_of_shift='{end_of_shift}'
                    WHERE id_attemdant='{id_attemdant}';
                """.format(
                    first_name=first_name,
                    last_name=last_name,
                    middle_name=middle_name,
                    start_of_shift=start_of_shift,
                    end_of_shift=end_of_shift,
                    id_attemdant=id_attemdant
                )

                self.__sqlDriver.exec_request(req)



    def remove_by_id(self, id_attemdant):

        req = """
            DELETE FROM Attemdants
            WHERE id_attemdant='{id_attemdant}'
        """.format(
            id_attemdant=id_attemdant
        )

        self.__sqlDriver.exec_request(req)




    def select_by_id(self, id_attemdant):

        req = """
            SELECT *
            FROM Attemdants
            WHERE id_attemdant='{id_attemdant}';
        """.format(id_attemdant=id_attemdant)

        self.__sqlDriver.exec_request(req)

        return self.__sqlDriver.fetchone()




    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Attemdants;
            """
        )

        return self.__sqlDriver.fetchall()


    