# Car Data Analysis Project

## Overview
This project performs data cleaning and analysis on car sales data stored in a MySQL database. The pipeline includes:
1. Connecting to a MySQL database.
2. Cleaning raw car sales data.
3. Loading cleaned data into MySQL.
4. Performing exploratory data analysis (EDA) and visualizing insights.

## Project Structure
- **README.md** - Project documentation  
- **config.ini** - Configuration file for database connection and file paths  
- **data/** - Folder containing raw CSV data  
- **data_analysis.py** - Performs EDA and generates visualizations  
- **data_cleaning.py** - Cleans raw data from CSV file  
- **db_connection.py** - Establishes connection to MySQL database  
- **load_data.py** - Loads cleaned data into MySQL database  
- **plots/** - Folder storing generated plots  
- **requirements.txt** - List of required dependencies  

## Prerequisites
Ensure you have Python installed (preferably Python 3.x). Install dependencies using:
pip install -r requirements.txt

## Configuration
Update `config.ini` with your MySQL database credentials and data file path:

[config]
host = 127.0.0.1
user = your_username
password = your_password
file_path = "./data/combined_data.csv"

## Usage

### Step 1: Establish Database Connection
Run `db_connection.py` to connect to the MySQL database:

python db_connection.py


### Step 2: Clean Data
Run `data_cleaning.py` to clean and preprocess the dataset:

python data_cleaning.py

### Step 3: Load Data into MySQL
Run `load_data.py` to create database, table and insert the cleaned data into the MySQL database:

python load_data.py


### Step 4: Analyze Data
Run `data_analysis.py` to perform exploratory data analysis and generate plots:

python data_analysis.py


This script will:
- Load cleaned data from MySQL.
- Generate statistical summaries.
- Visualize price distributions, mileage vs. price relationships, and more.
- Save all plots in the `plots/` directory.

## Output
The following visualizations are saved in the `plots/` folder:
- `price_distribution.png` - Car price distribution histogram.
- `mileage_vs_price.png` - Scatter plot of mileage vs. price.
- `mileage_vs_price_outliers.png` - Identifies outliers in mileage vs. price.
- `top_car_models.png` - Bar chart of the top 10 most common car models.
- `price_by_condition.png` - Box plot of car price distribution by condition.
- `Feature_Correlation_Heatmap.png` - Heatmap showing feature correlations.

## Notes
- Ensure MySQL server is running and the database `car_db` exists before executing the `data_analysis.py`.
- Modify queries in `data_analysis.py` if table names differ in your database.

## License
This project is for educational purposes. Feel free to modify and use it as needed.

## Author
Abhinaya

