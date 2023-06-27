#pandas
import pandas as pd

# Read Excel file
df = pd.read_excel('your_file.xlsx')

# Display the DataFrame
print(df)

#pyspark/sql
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Read Excel file
df = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("your_file.xlsx")

# Display the DataFrame
df.show()


