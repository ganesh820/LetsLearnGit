

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql import SQLContext



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spark = SparkSession.builder.appName("abc").getOrCreate()


    def read_from_mysql_db(table_name, db_name):
        df1 = spark.read.format('jdbc').options(
            url='jdbc:mysql://localhost/' + db_name,
            driver='com.mysql.jdbc.Driver',
            dbtable=table_name,
            user='root',
            password='root').load()
        return df1


    source_df = read_from_mysql_db('sys_config', 'sys')
    source_df.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
