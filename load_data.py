import pandas as pd
from db_connection import create_db_connection
from data_cleaning import clean_data
import configparser

config = configparser.ConfigParser()
config.read("config.ini") 
file_path = config["config"]["file_path"]

def insert_data_to_db(file_path):
    # Step 1: Create a database connection
    mydb = create_db_connection()
    if mydb is None:
        print("Database connection failed. Exiting.")
        return
    
    cursor = mydb.cursor()

    # Step 2: Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS car_db;")
    cursor.execute("USE car_db;")  # Switch to the car_database
    mydb.database = 'car_db'  # Ensure we're working with the correct DB
    
    # Step 3: Create the table if it doesn't exist (note the use of backticks for `condition`)
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS car_details (
        id INT AUTO_INCREMENT PRIMARY KEY,
        car_model VARCHAR(255),
        `condition` VARCHAR(50),  -- Escaping reserved keyword
        mileage FLOAT,
        price_usd FLOAT,
        monthly_payment FLOAT,
        dealer_name VARCHAR(255)
    );
    '''
    cursor.execute(create_table_query)
    print("Table created successfully!")
    mydb.commit()

    # Step 4: Clean the data from the CSV file
    df = clean_data(file_path)

    # Step 5: Insert data into the MySQL table
    insert_query = """
    INSERT INTO car_details (car_model, `condition`, mileage, price_usd, monthly_payment, dealer_name)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    
    for _, row in df.iterrows():
        
        # Handle any NaN or invalid values
        monthly_payment = row['Monthly Payment'] if pd.notna(row['Monthly Payment']) and row['Monthly Payment'] != "" else 0
    

        # Execute the insert query
        cursor.execute(insert_query, (
            row['Car Model'],
            row['Condition'],
            row['Mileage'] if pd.notna(row['Mileage']) else None,
            row['Price (USD)'] if pd.notna(row['Price (USD)']) else None,
            monthly_payment,
            row['Dealer Name'] if pd.notna(row['Dealer Name']) else None
        ))


    # Commit the changes to the database
    mydb.commit()
    cursor.close()
    mydb.close()

    print("Data inserted successfully into MySQL!")

# Call the function to insert data
insert_data_to_db(file_path)
