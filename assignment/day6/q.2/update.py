# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database ="smart_iot",
    use_pure = True
)

# form a query to be executed
id=int(input("enter a id:"))
moisture_level=float(input("enter a moisture_level to be updated:" ))
query=f"update sensor_readings SET moisture_level={moisture_level} WHERE id={id};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

