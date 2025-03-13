from pyspark.sql import SparkSession
from pyspark.sql.functions import col, window, to_timestamp

# Initialize Spark session
spark = SparkSession.builder.appName("FlightAggregator").getOrCreate()

# Load the data
df = spark.read.csv("C:\Users\venka\Downloads\flights.csv", header=True, inferSchema=True)

df = df.withColumn("flight_time", to_timestamp(col("flight_time")))


windowed_df = df.groupBy(
    window(col("flight_time"), "2 hours", "15 minutes") 
).count()

windowed_df.show()
