# example from spark website documentation
# https://spark.apache.org/docs/2.1.0/sql-programming-guide.html#sql

# data download location: https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

# everything in spark starts with the entry point SparkSession
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL basic example") \
    .config("spark.some.config.option","some-value") \
    .getOrCreate()

df = spark.read.csv("data\household_power_consumption.txt")
df.show()
