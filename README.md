sample-pyspark-job

Simple PySpark Job

Using Apache Spark to create a simple data pipeline - follows basic ETL structure - extracting data from csv, transforming local data through Spark SQL, and loading to filtered json file. Apache Spark is a framework which is used for processing, querying and analyzing Big data, disclaimer - definitely overkill for this particular application due to the low data volume. Spark requires quite a bit of overhead which makes it a less than ideal option for smaller datasets. 

Apache Spark is an open-source distributed general-purpose cluster-computing framework. Spark provides an interface for programming entire clusters with implicit data parallelism and fault tolerance.

<img width="645" alt="Screen Shot 2022-08-14 at 3 20 30 PM" src="https://user-images.githubusercontent.com/16201715/184556925-bb48450c-f220-4fcf-a9cf-5ca39c05e403.png">


Spark Core

It contains the basic functionality of Spark like task scheduling, memory management, interaction with storage, etc.

Spark SQL

It is a set of libraries used to interact with structured data. It used an SQL like interface to interact with data of various formats like CSV, JSON, Parquet, etc.

Spark Streaming

Spark Streaming is a Spark component that enables the processing of live streams of data. Live streams like Stock data, Weather data, Logs, and various others.

MLib
MLib is a set of Machine Learning Algorithms offered by Spark for both supervised and unsupervised learning
