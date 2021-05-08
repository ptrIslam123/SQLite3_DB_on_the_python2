#!/usr/bin/env python
#-*-coding: utf-8-*-

import vars 
from datetime import datetime


def get_time():
    return str(datetime.now())


def write_log(type_error, descr):
    with open(vars.SQL_SYSTEM_LOG_FILE_PATH, "a") as file:
        file.writelines(
            get_time() + "\t[" + type_error + "\t" + descr + "]\n"
        )
