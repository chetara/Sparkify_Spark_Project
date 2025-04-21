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

```
🚀 What It Does
This project is a full data engineering pipeline that:

✅ Reads raw JSON files of song and log data

✅ Cleans and transforms the data using PySpark

✅ Creates a star schema of the following tables:

songs (dimension)

artists (dimension)

users (dimension)

time (dimension)

songplays (fact table)

✅ Writes each table in Parquet format for optimized analytics

✅ Can be extended to run on AWS S3 + Redshift

🛠️ Technologies Used

Tool	Purpose
Python 3.10+	Core programming language
PySpark 3.x	Distributed data processing & transformation
Hadoop 3.3.1	File system layer (via winutils.exe on Windows)
Parquet	Columnar output format for performance
Local Filesystem	For testing (can easily move to cloud)
⚠️ Windows Fix: Native Hadoop Access Error
If you’re using Windows, Spark may crash when loading multiple files with a wildcard pattern due to missing native Hadoop support:

❌ Example Error
bash
Copy
Edit
java.lang.UnsatisfiedLinkError: org.apache.hadoop.io.nativeio.NativeIO$Windows.access0
✅ Fix Steps
Download winutils.exe for Hadoop 3.3.1:
winutils.exe (GitHub)

Place it in:

makefile
Copy
Edit
C:\hadoop\bin\winutils.exe
Set these environment variables in Python (before starting Spark):

python
Copy
Edit
import os
os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["SPARK_SUBMIT_OPTS"] = "-Dhadoop.home.dir=C:/hadoop"
Use Python’s glob module (instead of Spark's wildcard *.json):

python
Copy
Edit
import glob
file_paths = glob.glob("data/song_data/*/*/*/*.json")
file_paths = [f.replace("\\", "/") for f in file_paths]
df = spark.read.json(file_paths)
✅ This bypasses the native I/O crash and works on all systems.

🐍 How to Run the Project Locally
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/sparkify_spark_project.git
cd sparkify_spark_project
2. Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash or WSL
3. Install Required Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run Each ETL Step
bash
Copy
Edit
python etl/load_data.py
python etl/transform_songs.py
python etl/transform_users.py
python etl/build_songplays.py
📦 Output Tables
Each table is written to Parquet files under the outputs/ directory:

bash
Copy
Edit
outputs/
├── songs/
├── artists/
├── users/
├── time/
└── songplays/
You can inspect them with:

python
Copy
Edit
df = spark.read.parquet("outputs/songs/")
df.show()
🔮 Future Improvements
 Load outputs directly to Amazon S3

 Create external tables in Amazon Redshift or Athena

 Add Airflow DAGs for scheduling

 Include data validation and quality checks

 Build dashboard on top of output data using Power BI or Metabase

🙌 Author
Built with 💻 by @chetara
Inspired by the Udacity Data Engineering Nanodegree Sparkify project.

📜 License
MIT License – free to use and modify.

yaml
Copy
Edit

---

Let me know if you want to:
- Add badges (e.g., Python version, license, repo stars)
- Add a section for screenshots or schema diagrams
- Translate or localize the README (Arabic 🇩🇿 or French 🇫🇷?)

Your project is looking 🔥 and very polished!






You said:
commit the changes in git


ChatGPT said:
Great! Let’s commit your updated README.md and any other changes using Git. Here’s exactly what to do:

✅ Step-by-Step to Commit & Push
1. Make sure you’re in your project folder
bash
Copy
Edit
cd path/to/Sparkify_spark_project
2. Check Git status
See what files you’ve changed:

bash
Copy
Edit
git status
You should see README.md and maybe other changed files in red or green.

3. Add the updated files
If you only want to commit the README:

bash
Copy
Edit
git add README.md
Or if you want to add everything you’ve changed:

bash
Copy
Edit
git add .
4. Commit the changes
bash
Copy
Edit
git commit -m "📝 Update README with full ETL instructions and Windows fix"
5. Push to GitHub
Make sure your remote is set (you only need to do this once):

bash
Copy
Edit
git remote -v
You should see something like:

scss
Copy
Edit
origin  git@github.com:chetara/sparkify_spark_project.git (fetch)
origin  git@github.com:chetara/sparkify_spark_project.git (push)
If that looks good, then push:

bash
Copy
Edit
git push
✅ Result
Your changes are now live on GitHub! 🎉
Check: https://github.com/chetara/sparkify_spark_project

Let me know if:

You want to add a badge (like Python version)

Or build a simple visual schema diagram to add to your README next!







You said:
generate readme.md file for this project


ChatGPT said:
Sure! Here's your complete and ready-to-use README.md file for your Sparkify ETL Project — clean, professional, and markdown-formatted. Save this as README.md in the root of your project:

markdown
Copy
Edit
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