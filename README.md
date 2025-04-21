# 🎧 Sparkify ETL Project (PySpark)

This project builds a **data pipeline using Apache Spark** to process song and log data for Sparkify, a fictional music streaming service. The result is a set of **analytically useful tables** written in Parquet format, structured in a star schema.

---

## 📁 Project Structure

```bash
Sparkify_spark_project/
├── data/                  # Raw input data (songs & logs)
│   ├── song_data/
│   └── log_data/
├── etl/                   # ETL pipeline scripts
│   ├── test.py
│   ├── load_data.py
│   ├── transform_songs.py
│   ├── transform_users.py
│   ├── build_songplays.py
├── outputs/               # Output folder for Parquet tables
├── .venv/                 # Python virtual environment (excluded from git)
├── requirements.txt       # Python dependencies
└── README.md              # This file

``` 
# ⚙️ Spark Architecture Behind This ETL Project

This ETL pipeline is powered by **Apache Spark**, a distributed data processing engine. Even though this project runs locally, it uses the **same execution model** that powers Spark on clusters like AWS EMR, Databricks, and Hadoop YARN.

---

## 🧠 What Is Happening Under the Hood?

### ✅ Components Used by Spark:

| Component       | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| **Driver**      | Coordinates the job, builds the DAG, sends tasks to executors        |
| **Executors**   | Perform the actual data processing (reading, filtering, writing)     |
| **Cluster Manager** | Manages resources. In this project, it's `local[*]` (your own machine) |

```python
spark = SparkSession.builder.appName("Sparkify ETL").getOrCreate()
```

## 🚀 What It Does
✅ Reads raw JSON files of song and log data

✅ Cleans and transforms the data using PySpark

✅ Creates a star schema of tables:

songs (dimension)

artists (dimension)

users (dimension)

time (dimension)

songplays (fact table)

✅ Writes each table in Parquet format for efficient querying

## 🛠️ Technologies Used

Tool	Purpose
Python 3.10+	Core programming language
PySpark 3.x	Distributed data processing & transformation
Hadoop 3.3.1	Required for file I/O on Windows (via winutils.exe)
Parquet	Columnar output format for performance
Local filesystem	Storage backend (easily extendable to AWS)

## ⚠️ Windows Setup Fix: Native Hadoop Error
If you get this error when reading many files:


``` bash

java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0
✅ Solution

```

# ✅ Step-by-Step Fix:
Download winutils.exe

Download: winutils.exe (Hadoop 3.3.1)

Create Hadoop Directory


``` bash

C:\hadoop\bin\

``` 

Place the downloaded file


``` bash

C:\hadoop\bin\winutils.exe

```
Set Environment Variables in Python


``` python

import os
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"

```
Bypass native file globbing using Python


``` python

import glob
file_paths = glob.glob("data/song_data/*/*/*/*.json")
file_paths = [f.replace("\\", "/") for f in file_paths]
df = spark.read.json(file_paths)

```
## 🧪 ETL Process Breakdown
This project follows a classic ETL pipeline using Apache Spark. Here's a detailed breakdown of each phase:

# Step 1: Load Raw Data
➤ What
Load raw song and log data (JSON format) into Spark DataFrames.

➤ Why
To perform distributed processing and transformation at scale, Spark needs structured DataFrames.

➤ How
``` python
song_df = spark.read.json(song_files)
log_df = spark.read.json(log_files).filter(col("page") == "NextSong")
Used Python’s glob module to read file paths (helps on Windows)
```

Filtered log_df by page == "NextSong" to only include song play events

Saved raw datasets to Parquet (outputs/raw_logs/, outputs/raw_songs/)

# Step 2: Transform Song & Artist Tables
➤ What
Extract clean, structured dimension tables: songs and artists.

➤ Why
To enable analysis by song, artist, and metadata like duration, year, etc.

➤ How
``` python
songs_table = song_df.select("song_id", "title", "artist_id", "year", "duration").dropDuplicates()
artists_table = song_df.select("artist_id", "artist_name", "artist_location", ...).dropDuplicates()
``` 
Ensured uniqueness with .dropDuplicates()

Wrote to outputs/songs/ and outputs/artists/

# Step 3: Transform Users & Time Tables
➤ What
Create users and time tables from the log dataset.

➤ Why
Useful for analyzing user behavior and session time trends.

➤ How
``` python

users_table = log_df.select("userId", "firstName", "lastName", ...).dropDuplicates()

get_timestamp = udf(lambda ts: datetime.fromtimestamp(ts / 1000))
log_df = log_df.withColumn("start_time", get_timestamp("ts"))
time_table = log_df.select("start_time").withColumn("hour", hour("start_time"))...
```
Used Spark’s udf to convert timestamps

Extracted time components: hour, day, week, etc.

Saved to outputs/users/ and outputs/time/

# Step 4: Build Songplays Fact Table
➤ What
Create the central fact table songplays by joining logs with songs and artists.

➤ Why
To enable deep analysis like:

Top songs/artists by plays

User behavior over time

Song popularity by location/session

➤ How
``` python

songplays_df = log_df.join(songs_df, ...).join(artists_df, ...)

songplays_df = songplays_df.withColumn("songplay_id", monotonically_increasing_id())
Performed joins on song == title and length == duration
```

Generated songplay_id with monotonically_increasing_id()

Wrote to outputs/songplays/
## 🙌 Author
Built by @chetara
Inspired by the Udacity Data Engineer Nanodegree Sparkify project.