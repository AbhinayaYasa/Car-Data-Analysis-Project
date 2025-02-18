from db_connection import create_db_connection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

## Connect to MySQL database
conn = create_db_connection()

if conn is None:
    print("Database connection failed. Exiting.")
    exit()

cursor = conn.cursor()
cursor.execute("USE car_db;")  #select database

# Loading cleaned data into Pandas DataFrame
query = "SELECT * FROM car_details;"
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Display first few rows
print(df.head())

# Check data types and missing values
print(df.info())
print(df.isnull().sum())

# Summary statistics
print(df.describe())

# Check unique values in 'condition'
print(df['condition'].value_counts())

# Check number of unique car models
print(f"Number of unique car models: {df['car_model'].nunique()}")

output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)


plt.figure(figsize=(10, 8))
sns.histplot(df['price_usd'], bins=50, kde=True, color="blue")
plt.title("Car Price Distribution")
plt.xlabel("Price (USD)")
plt.ylabel("Frequency")
plt.grid(True)
# Annotate the highest frequency bin
max_freq = df['price_usd'].value_counts().max()
max_bin = df['price_usd'].value_counts().idxmax()
plt.annotate(f'Highest Frequency Bin: {max_bin}', xy=(max_bin, max_freq), xytext=(max_bin, max_freq * 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10)
plt.yscale("linear")
# Setting x-axis limits as most of the car prices around $200,000 have the highest count in the dataset
plt.xlim(0, 200000)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "price_distribution.png"))
plt.close()



plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(data=df, x='mileage', y='price_usd', hue='condition', palette='coolwarm')
# Highlight outliers with high price and high mileage
outliers = df[(df['mileage'] > 100000) & (df['price_usd'] > 100000)]
sns.scatterplot(data=outliers, x='mileage', y='price_usd', color='green', marker='x', s=100, label='Outliers')
for _, row in outliers.iterrows():
    plt.annotate('Outlier', xy=(row['mileage'], row['price_usd']), xytext=(row['mileage']+20000, row['price_usd']),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='green')
plt.title("Mileage vs Price")
plt.xlabel("Mileage (miles)")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.legend(title="Condition")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "mileage_vs_price.png"))
plt.close()


#mileage_vs_price_outliers
dataframe = pd.DataFrame({
    'mileage': [50000, 150000, 200000, 250000, 300000],
    'price_usd': [20000, 150000, 250000, 300000, 400000],
})
plt.figure(figsize=(12, 8))
scatter = sns.scatterplot(data=dataframe, x='mileage', y='price_usd', palette='coolwarm')
outliers = dataframe[(dataframe['mileage'] > 100000) & (dataframe['price_usd'] > 100000)]
# Plot the outliers separately
sns.scatterplot(data=outliers, x='mileage', y='price_usd', color='green', marker='x', s=100, label='Outliers')
# Annotate the outliers
for _, row in outliers.iterrows():
    plt.annotate('Outlier', xy=(row['mileage'], row['price_usd']), xytext=(row['mileage']+20000, row['price_usd']+10000),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='green')
plt.title("Mileage vs Price")
plt.xlabel("Mileage (miles)")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "mileage_vs_price_outliers.png"))
plt.close()


plt.figure(figsize=(12, 6))
top_models = df['car_model'].value_counts().head(10)
top_models.plot(kind='bar', color='purple')
plt.title("Top 10 Most Common Car Models")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right", fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # This helps to adjust the plot to fit into the figure area.
plt.savefig(os.path.join(output_dir, "top_car_models.png"))
plt.close()


plt.figure(figsize=(12,8))
sns.boxplot(x=df['condition'], y=df['price_usd'], palette="coolwarm")
plt.title("Car Price Distribution by Condition")
plt.xlabel("Condition")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig(os.path.join(output_dir, "price_by_condition.png"))
plt.close()

plt.figure(figsize=(10,6))
sns.scatterplot(x=df['price_usd'], y=df['monthly_payment'], color="green")
plt.title("Monthly Payment vs. Price")
plt.xlabel("Price (USD)")
plt.ylabel("Monthly Payment (USD)")
plt.grid(True)
plt.savefig(os.path.join(output_dir, "price_by_condition.png"))
plt.close()

# Compute correlation matrix
corr = df[['mileage', 'price_usd', 'monthly_payment']].corr()

# Heatmap
plt.figure(figsize=(8,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.savefig(os.path.join(output_dir, "Feature_Correlation_Heatmap.png"))
plt.close()