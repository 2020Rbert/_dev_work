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

def read_db():
    with connect_db() as cnx:
        try:
            cursor = cnx.cursor()
            #! hardcoded -- tablename
            cursor.execute("""SELECT * FROM laptop_test""")
            results = cursor.fetchall()
            # for row in results:
            #     print(row)
            return results
        except mysql.connector.Error as e:
            print(f"Error:{e}")
            return []

