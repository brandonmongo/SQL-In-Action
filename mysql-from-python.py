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
        cursor.execute("update Friends set age = %s where name = %s;",
                       (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was succussful
    connection.close()
