import mysql.connector
import configparser

def create_db_connection():
    
    try:
        # Load database configuration
        config = configparser.ConfigParser()
        config.read("config.ini") 

        host = config["config"]["host"]
        user = config["config"]["user"]
        password = config["config"]["password"]

        # Establish database connection
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
        
        )
        print("Connected to MySQL successfully!")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
