from pyspark.sql import SparkSession
from pyspark.sql import SQLContext


if __name__ == '__main__':
    scSpark = SparkSession \
        .builder \
        .appName("reading csv") \
        .getOrCreate()
        
data_file = '/Users/development/Desktop/data.csv'

sdfData = scSpark.read.csv(data_file, header=True, sep=",").cache()

sdfData.registerTempTable("sales")

output =  scSpark.sql('SELECT * FROM sales WHERE index > 10')

output.write.format('json').save('filtered.json')    