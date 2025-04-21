import os
import glob
from pyspark.sql import SparkSession

# Fix for Spark on Windows
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"

def load_data():
    print(" Starting Sparkify ETL - Load Raw Data")

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Sparkify ETL - Load Data") \
        .getOrCreate()

    # Load song_data
    song_files = glob.glob("data/song_data/*/*/*/*.json", recursive=True)
    song_files = [f.replace("\\", "/") for f in song_files]

    if not song_files:
        print(" No song files found.")
    else:
        print(f" Found {len(song_files)} song files.")
        song_df = spark.read.json(song_files)
        print(f" Song data loaded: {song_df.count()} rows")

        song_output_path = "outputs/raw_songs/"
        song_df.coalesce(1).write.mode("overwrite").parquet(song_output_path)
        print(f" Song data written to {song_output_path}")

    # Load log_data
    log_files = glob.glob("data/log_data/*/*/*.json", recursive=True)
    log_files = [f.replace("\\", "/") for f in log_files]

    if not log_files:
        print(" No log files found.")
    else:
        print(f" Found {len(log_files)} log files.")
        log_df = spark.read.json(log_files)
        print(f" Log data loaded: {log_df.count()} rows")

        log_output_path = "outputs/raw_logs/"
        log_df.coalesce(1).write.mode("overwrite").parquet(log_output_path)
        print(f"Log data written to {log_output_path}")

    print(" ETL Load Phase Complete.")

if __name__ == "__main__":
    load_data()
