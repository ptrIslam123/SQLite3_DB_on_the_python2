#! /usr/bin/env python

import sqliteDriver as sql
from vars import *


class Monitoring_Center_of_Emergency:

    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/monitoring_center_of_emergency.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )
        self.__sqlDriver.exec_file(
            "{SQL_SCRIPOTS_DIR_PATH}/monitoring_center_of_emergency.txt".format(
                SQL_SCRIPOTS_DIR_PATH=SQL_SCRIPOTS_DIR_PATH
            )
        )



    def insert(self,
            id_emergency,
            data,
            time,
            location,
            conclusion):

            req = """INSERT INTO Monitoring_Center_of_Emergency
                    (id_emergency, data, time, location, conclusion)
                    VALUES 
                    ('{id_emergency}', '{data}', '{time}', '{location}', '{conclusion}');""".format(
                        id_emergency=id_emergency, 
                        data=data, 
                        time=time, 
                        location=location, 
                        conclusion=conclusion
                    )
                    
            self.__sqlDriver.exec_request(
                req
            )



    def update_by_id(self,
                id_emergency,
                data,
                time,
                location,
                conclusion):

                req = """
                    UPDATE Monitoring_Center_of_Emergency
                    SET
                    data='{data}',
                    time='{time}',
                    location='{location}',
                    conclusion='{conclusion}'
                    WHERE id_emergency='{id_emergency}';
                """.format(
                    data=data,
                    time=time,
                    location=location,
                    conclusion=conclusion,
                    id_emergency=id_emergency
                )

                self.__sqlDriver.exec_request(req)



    def remove_by_id(self, id_emergency):

        req = """
            DELETE FROM Monitoring_Center_of_Emergency
            WHERE id_emergency='{id_emergency}'
        """.format(
            id_emergency=id_emergency
        )

        self.__sqlDriver.exec_request(req)




    def select_by_id(self, id_emergency):

        req = """
            SELECT *
            FROM Monitoring_Center_of_Emergency
            WHERE id_emergency='{id_emergency}';
        """.format(id_emergency=id_emergency)

        self.__sqlDriver.exec_request(req)

        return self.__sqlDriver.fetchone()




    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Monitoring_Center_of_Emergency;
            """
        )

        return self.__sqlDriver.fetchall()


    