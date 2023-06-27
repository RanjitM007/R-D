#####Pandas:
'''Pandas is a powerful data manipulation library in Python. To read a CSV file using Pandas, you can use the read_csv() function. Here's an example: 
'''


import pandas as pd

# Read CSV file
df = pd.read_csv('file.csv')
  #In the above code, file.csv is the name of the CSV file you want to read. Pandas will read the file and store the data in a DataFrame (df in this case).

####PySpark:
##PySpark is the Python API for Apache Spark, a distributed computing framework. To read a CSV file using PySpark, you can use the spark.read.csv() method. Here's an example:

from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.getOrCreate()

# Read CSV file
df = spark.read.csv('file.csv', header=True, inferSchema=True)
#In the above code, file.csv is the name of the CSV file you want to read. The header=True argument indicates that the first row contains column names, and inferSchema=True attempts to infer the data types of each column.
