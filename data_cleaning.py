import pandas as pd

def clean_data(file_path):
 
    df = pd.read_csv(file_path)

    # Clean 'Mileage' column
    df['Mileage'] = (
        df['Mileage']
        .astype(str)
        .str.replace(' mi.', '', regex=True)
        .str.replace(',', '')
    )
    df['Mileage'] = pd.to_numeric(df['Mileage'], errors='coerce')

    # Clean 'Price (USD)' column
    df['Price (USD)'] = df['Price (USD)'].astype(str).str.replace(r'[\$,]', '', regex=True)
    df['Price (USD)'] = pd.to_numeric(df['Price (USD)'], errors='coerce')

    
    # Remove non-numeric characters (except dot)
    df['Monthly Payment'] = df['Monthly Payment'].astype(str).str.replace(r'[^\d]', '', regex=True)
    df['Monthly Payment'] = pd.to_numeric(df['Monthly Payment'], errors='coerce')


    # Fill NaN values with None (for MySQL NULL support)
    df = df.where(pd.notna(df), None)

    return df
