import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime, hour, dayofmonth, weekofyear, month, year, dayofweek

# Java + Hadoop path setup (for Windows)
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"
os.environ["JAVA_HOME"] = "C:/Java/jdk-11"
os.environ["PATH"] = f"{os.environ['JAVA_HOME']}\\bin;" + os.environ["PATH"]

def transform_users():
    print(" Starting users & time transformation...")

    spark = SparkSession.builder \
        .appName("Sparkify Transform Users") \
        .master("local[*]") \
        .getOrCreate()

    #  Load raw logs
    log_df = spark.read.parquet("outputs/raw_logs/")
    print(f" Log rows: {log_df.count()}")

    #  Users Table
    users_table = log_df.filter(col("page") == "NextSong") \
        .selectExpr(
            "userId as user_id",
            "firstName as first_name",
            "lastName as last_name",
            "gender",
            "level"
        ).dropDuplicates(["user_id"])

    users_table.write.mode("overwrite").parquet("outputs/users/")
    print(" Users table written")

    #  Time Table
    time_df = log_df \
        .withColumn("start_time", (col("ts") / 1000).cast("timestamp")) \
        .filter(col("page") == "NextSong") \
        .select("start_time") \
        .dropDuplicates()

    time_table = time_df \
        .withColumn("hour", hour(col("start_time"))) \
        .withColumn("day", dayofmonth(col("start_time"))) \
        .withColumn("week", weekofyear(col("start_time"))) \
        .withColumn("month", month(col("start_time"))) \
        .withColumn("year", year(col("start_time"))) \
        .withColumn("weekday", dayofweek(col("start_time")))

    time_table.write.mode("overwrite").parquet("outputs/time/")
    print("Time table written")

    spark.stop()
    print("Users & Time transformation complete.")

if __name__ == "__main__":
    transform_users()
