# import Flask class from flask module
from flask import Flask, request
from datetime import datetime


from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor')
def create_sensor():
    # extract data form form
    id = request.form.get('id')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    # create a query to add student into table
    query = f"insert into sensor_readings values({id}, '{temp}', '{humidity}', '{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "sensor is added successfully"

@server.get('/sensor')
def retrieve_sensor():
    # create a select query
    query = "select * from sensor_readings;"

    # execute select query
    data = executeSelectQuery(query=query)

    return f"sensor_readings : {data}"

@server.put('/sensor')
def update_sensor():
    # extract data form form
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')

    # create a query
    query = f"update sensor_readings SET temp = '{temp}' where humidity = '{humidity}';"

    # execute the query
    executeQuery(query=query)

    return " temp is updated successfully"

@server.delete('/sensor')
def delete_sensor():
    # extract data form form
    temp = request.form.get('temp')

    # create a query
    query = f"delete from sensor_readings where temp = '{temp}';"

    # execute the query
    executeQuery(query=query)

    return "sensor is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)