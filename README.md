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

## 🙌 Author
Built by @chetara
Inspired by the Udacity Data Engineer Nanodegree Sparkify project.