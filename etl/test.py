import os
import glob
from pyspark.sql import SparkSession

#  Set environment (just in case)
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"

#  Manually collect files instead of Spark globbing
file_paths = glob.glob("data/song_data/*/*/*/*.json")
file_paths = [f.replace("\\", "/") for f in file_paths]  # normalize Windows paths

#  Create Spark session (no need to force config override now)
spark = SparkSession.builder \
    .appName("Sparkify Test - Songs") \
    .getOrCreate()

print(" Spark session started")
print(f" Files to load: {len(file_paths)}")

#  Read files from the list
df = spark.read.json(file_paths)

print("Data loaded")
df.printSchema()
df.show(5, truncate=False)
