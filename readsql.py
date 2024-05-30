import os

import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASSWORD')

connection = mysql.connector.connect(host=host,
                                     user=username,
                                     password=password,
                                     database='swiftmarket')

cursor = connection.cursor()

def queryToDataFrame(query):

    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df




def describeTable(tablename):
    query = f"""DESCRIBE {tablename};"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df
