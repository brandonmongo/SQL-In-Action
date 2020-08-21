import os
import pymysql

# Get username from Gitpod workspace

username = os.getenv("C9_USER")

# Connect to the database
# connection object to connect to the database
connection = pymysql.connect(host="localhost",
                             user=username,
                             password="",
                             db="Chinook")

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the
        # table already exist
finally:
    # Close the connection, regardless of whether the above was succussful
    connection.close()
