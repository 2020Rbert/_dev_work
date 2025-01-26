import mysql.connector
import logging as log
import uuid
from datetime import datetime

log.basicConfig(
    level=log.INFO,
    format="%(asctime)s |--%(levelname)s - %(message)s"
)


db_config = {
    'host' : "localhost",
    'port' : 3306,
    'user' : 'root',
    'database' : "data_management",
    #! SET ENVIROMENTVARIALBES
    'password' : "azsxdcf"   
}

def connect_db():
    try:
        cnx = mysql.connector.connect(**db_config)
        log.info("Successfully connected!")
        return cnx        
    except mysql.connector.Error as err:
        log.info(f"Error to connect: {err}")
    
def close_db(cnx):
    if cnx:
        try:
            cnx.close()
            log.info("Connection closed!")
        except mysql.connector.Error as e:
            log.error(f"Error closing connection! Error: {e}")
        
        
#? CRUD METHODEN IMPLEMETIEREN

def read_db():
        cnx = connect_db()
        try:
            cursor = cnx.cursor()
            #! hardcoded -- tablename
            cursor.execute("""SELECT * FROM laptop_test""")
            results = cursor.fetchall()
            # for row in results:
            #     print(row)
            return results
        except mysql.connector.Error as e:
            log.error(f"Error:{e}")
            return []
        finally:
            close_db(cnx)

def write_db(model, username, layout):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        
        # Debug-Ausgabe
        print(f"Inserting: model={model}, username={username}, layout={layout}")
        
        cursor.execute(
            "INSERT INTO laptop_test (model, name, kbd_layout) VALUES (%s, %s, %s)",
            (model, username, layout)
        )
        
        connection.commit()
        cursor.close()
        connection.close()
        return True
        
    except Exception as e:
        print(f"Database error: {str(e)}")  # Debug-Ausgabe
        return False
        