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
        row = ("Bob", 21, "1999-02-06 23:04:56")
        cursor.execute("insert into Friends values (%s, %s, %s);", row)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was succussful
    connection.close()
