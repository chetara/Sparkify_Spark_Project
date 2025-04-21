import os
import glob
from pyspark.sql import SparkSession

#  Fix for Spark on Windows (native Hadoop issue)
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"

def load_data():
    print(" Starting Sparkify ETL - Load Raw Data")

    #  Spark Session in local mode
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Sparkify ETL - Load Data") \
        .getOrCreate()

    #  Load song_data files using glob (cross-platform compatible)
    song_files = glob.glob("data/song_data/*/*/*/*.json", recursive=True)
    song_files = [f.replace("\\", "/") for f in song_files]  # Fix Windows path separators

    if not song_files:
        print(" No song files found.")
    else:
        print(f" Found {len(song_files)} song files.")
        song_df = spark.read.json(song_files)
        print(f" Song data loaded: {song_df.count()} rows")

        # Optional: use .coalesce(1) to reduce memory usage (disable for large datasets)
        
        output_path = "outputs/raw_logs/"
        song_df.coalesce(1).write.mode("overwrite").parquet(output_path)
        print(f" Song data written to {output_path}")

   

if __name__ == "__main__":
    load_data()
