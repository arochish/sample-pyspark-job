sample-pyspark-job

Simple PySpark Job

Using Apache Spark to create a simple data pipeline - follows basic ETL structure - extracting data from csv, transforming local data through Spark SQL, and loading to filtered json file. Apache Spark is a framework which is used for processing, querying and analyzing Big data, disclaimer - definitely overkill for this particular application due to the low data volume. Spark requires quite a bit of overhead which makes it a less than ideal option for smaller datasets. 



Spark Core

It contains the basic functionality of Spark like task scheduling, memory management, interaction with storage, etc.

Spark SQL

It is a set of libraries used to interact with structured data. It used an SQL like interface to interact with data of various formats like CSV, JSON, Parquet, etc.

Spark Streaming

Spark Streaming is a Spark component that enables the processing of live streams of data. Live streams like Stock data, Weather data, Logs, and various others.

MLib
MLib is a set of Machine Learning Algorithms offered by Spark for both supervised and unsupervised learning
