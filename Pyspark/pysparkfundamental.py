import pyspark as spark
from pyspark.sql import SparkSession

spark = spark = SparkSession.builder \
   .appName("PySparkFundamentals") \
   .master("local[*]") \
   .getOrCreate()
data = [(1,"Alice","HR",5000),
        (2,"Bob","IT",6000),
        (3,"Charlie","HR",7000),
        (4,"David","IT",8000),
        (5,"Eve","Finance",9000)]
columns = ["id","name","department","salary"]

df = spark.createDataFrame(data,columns)
# df.select("name","salary").show()
# df.filter(df.department == "IT").show()
# df.show()E
# df.printSchema()
df_select = df.select("name","salary")
df_filter = df.filter(df.department == "IT")
# df_select.show()
# df_filter.show()
df.withColumn('bonus',df.salary*0.20)
# df.show()
new_df = df.withColumn('bonus',df.salary*0.20)
# new_df.show()
# df.groupBy("department").sum("salary").show()
# df.groupBy("department").avg("salary").show()
# df.groupBy("department").count().show()
# df.groupBy("department").agg({"salary":"sum"}).show()
# df.groupBy("department").agg({"salary":"avg"}).show()
# df.groupBy("department").agg({"salary":"count"}).show()
df.groupBy("department").count().explain()
df.filter(df.department == 'IT').explain()