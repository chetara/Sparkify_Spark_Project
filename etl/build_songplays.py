import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, monotonically_increasing_id

# Setup for Spark on Windows
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"
os.environ["JAVA_HOME"] = "C:/Java/jdk-11"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}\\bin;" + os.environ["PATH"]

def build_songplays():
    print(" Starting fact table: songplays...")

    spark = SparkSession.builder \
        .appName("Sparkify Build Songplays") \
        .master("local[*]") \
        .getOrCreate()

    # Load raw logs and dimension tables
    logs_df = spark.read.parquet("outputs/raw_logs/").filter(col("page") == "NextSong")
    songs_df = spark.read.parquet("outputs/songs/")
    artists_df = spark.read.parquet("outputs/artists/")

    # Drop duplicate column from artists to avoid ambiguity
    artists_df = artists_df.drop("location")  # optional if already dropped

    # Join logs -> songs -> artists
    songplays_df = logs_df \
        .join(songs_df, (logs_df.song == songs_df.title) & (logs_df.length == songs_df.duration), how="left") \
        .join(artists_df, songs_df.artist_id == artists_df.artist_id, how="left") \
        .withColumn("start_time", (col("ts") / 1000).cast("timestamp")) \
        .withColumn("songplay_id", monotonically_increasing_id()) \
        .drop(artists_df.artist_id)  #  fix ambiguity

    # Select and rename columns for the fact table
    fact_table = songplays_df.select(
        col("songplay_id"),
        col("start_time"),
        col("userId").alias("user_id"),
        col("level"),
        col("song_id"),
        col("artist_id"),
        col("sessionId").alias("session_id"),
        col("location"),
        col("userAgent").alias("user_agent")
    )

    # Save the final songplays table to Parquet
    fact_table.write.mode("overwrite").parquet("outputs/songplays/")
    print(" Songplays table written successfully.")

    spark.stop()

if __name__ == "__main__":
    build_songplays()
