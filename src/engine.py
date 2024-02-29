from pyspark.sql import SparkSession

spark = (SparkSession.builder
         .master("local[1]")
         .appName("PySpark Tutorial")
         .getOrCreate())

df = spark.read.format("csv").option("header",True).load("../data/example-source.csv")
# df.printSchema()

df.toPandas().to_csv("../data/example-target.csv", header=True, index=False)

print(f'--- {spark.sparkContext.applicationId} ---')
print(f'--- {spark.sparkContext.appName} ---')
print("Spark version: ", spark.version)
