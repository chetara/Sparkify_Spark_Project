import os
import subprocess

# Ensure Java is properly linked inside Python
os.environ["JAVA_HOME"] = "C:/Java/jdk-11"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}\\bin;" + os.environ["PATH"]

print("JAVA_HOME =", os.environ["JAVA_HOME"])
subprocess.run(["java", "-version"], check=True)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def transform_songs():
    print(" Starting song & artist transformation...")

    spark = SparkSession.builder \
        .appName("Sparkify Transform Songs") \
        .master("local[*]") \
        .getOrCreate()

    song_df = spark.read.parquet("outputs/raw_songs/")

    # Songs Table
    songs_table = song_df.select(
        "song_id", "title", "artist_id", "year", "duration"
    ).dropDuplicates(["song_id"])

    songs_table.write.mode("overwrite").parquet("outputs/songs/")
    print(" Songs table written")

    # Artists Table
    artists_table = song_df.selectExpr(
        "artist_id",
        "artist_name as name",
        "artist_location as location",
        "artist_latitude as latitude",
        "artist_longitude as longitude"
    ).dropDuplicates(["artist_id"])

    artists_table.write.mode("overwrite").parquet("outputs/artists/")
    print(" Artists table written")

    spark.stop()
    print(" Transformation complete.")

if __name__ == "__main__":
    transform_songs()
