# 🎧 Sparkify ETL Project (PySpark)

This project builds a **data pipeline using Apache Spark** to process song and log data for Sparkify, a fictional music streaming service. The result is a set of **analytically useful tables** written in Parquet format, structured in a star schema.

---

## 📁 Project Structure

```bash
Sparkify_spark_project/
├── data/
│   ├── song_data/
│   └── log_data/
├── etl/
│   ├── load_data.py
│   ├── transform_songs.py
│   ├── transform_users.py
│   ├── build_songplays.py
├── outputs/
├── .venv/
├── requirements.txt
└── README.md


##  🚀 What It Does
Reads raw JSON files of song and log data

Cleans and transforms them using PySpark

Creates the following tables:

songs

artists

users

## time

songplays

Outputs results to parquet files in /outputs

## Technologies Used
Python 3.10+

PySpark 3.x

Hadoop 3.3.1 (via winutils.exe for Windows users)

Local filesystem (optional: S3/Redshift for scaling later)


### 🚨 Windows Note: Native Hadoop Error Fix

To avoid `NativeIO$Windows.access0` crash when reading many files on Windows:
- Use Python's `glob` module to list files
- Pass them directly to `spark.read.json([...])`
