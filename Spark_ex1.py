# https://www.datacamp.com/community/tutorials/apache-spark-tutorial-machine-learning

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Linear Regression Model") \
    .config("spark.executor.memory", "1gb") \
    .getOrCreate

# sc = spark.sparkContext

rdd = spark.sparkContext.textFile('C:/Users/ugyh17/Documents/Python Scripts/Spark_App_Test/data/cal_housing.data')

###################
# stopped because the ex uses RDD. wanted to learn DataFrame first.

spark.stop()