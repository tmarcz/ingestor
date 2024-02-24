from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .master("local")
         .appName("PySpark Tutorial")
         .getOrCreate())


print(f'--- {spark.sparkContext.applicationId} ---')
print(f'--- {spark.sparkContext.appName} ---')
print("Spark version: ", spark.version)
