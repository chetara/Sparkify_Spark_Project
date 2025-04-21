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