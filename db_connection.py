import mysql.connector
from contextlib import contextmanager

config = {
    'host' : "localhost",
    'port' : 3306,
    'user' : 'root',
    'database' : "data_management",
    #! SET ENVIROMENTVARIALBE
    'password' : "azsxdcf"   
}
#? Conetextmanger means -- WITH STATEMENT --

@contextmanager
def connect_db():
    try:
        cnx = mysql.connector.connect(**config)
        print("Successfully connected!")
        yield cnx
        
    except mysql.connector.Error as err:
        print(f"Error to connect: {err}")
    
    finally:
        cnx.close()
        print("Connection closed!")
        
#? CRUD METHODEN IMPLEMETIEREN

def read():
    connect_db()