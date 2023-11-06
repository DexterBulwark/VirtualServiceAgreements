"""
This is here just in case you need to connect to a database. I am thinking the wording might be stored there eventually.
"""

import pyodbc
import json


def load_config(filename="db_config.json"):
    with open(filename, "r") as f:
        return json.load(f)


config = load_config()


def connect_to_vsql3(intent="ReadOnly"):  # Should only ever need ReadOnly for this
    pdo = None

    vsql3_config = config["vsql3"]
    host = vsql3_config["host"] + "," + vsql3_config["port"]
    username = vsql3_config["username"]
    password = vsql3_config["password"]
    dbname = vsql3_config["dbname"]

    connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={host};DATABASE={dbname};UID={username};PWD={password};ApplicationIntent={intent}"

    try:
        pdo = pyodbc.connect(connection_string)
    except pyodbc.InterfaceError as ie:
        error_code = ie.args[0]
        error_message = ie.args[1] if len(ie.args) > 1 else "InterfaceError"
        print(
            f"connectToVSQL3: Database Interface Error. Error code: {error_code}, Error Message: {error_message}"
        )
        return None
    except pyodbc.OperationalError as oe:
        error_code = oe.args[0]
        error_message = oe.args[1] if len(oe.args) > 1 else "OperationalError"
        print(
            f"connectToVSQL3: Operational Error in database connection. Error code: {error_code}, Error Message: {error_message}"
        )
        return None
    except pyodbc.Error as e:
        error_code = e.args[0]
        error_message = e.args[1] if len(e.args) > 1 else "GeneralError"
        print(
            f"connectToVSQL3: General Database Error. Error code: {error_code}, Error Message: {error_message}"
        )
        return None
    except Exception as ex:
        print(f"connectToVSQL3: An unexpected error occurred: {ex}")
        return None

    return pdo
