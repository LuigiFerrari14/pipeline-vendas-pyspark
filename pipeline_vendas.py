# Databricks notebook source
df_raw = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Workspace/Users/rogeriomendess2018@gmail.com/pipeline-vendas-pyspark/data/vendas.csv")
)

df_raw.display()

# COMMAND ----------

from pyspark.sql.functions import col, trim, to_date

df_clean = (
    df_raw
    .filter(col("order_id").isNotNull())
    .filter(trim(col("product")) != "")
    .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))
)

df_clean.display()

# COMMAND ----------

from pyspark.sql.functions import col

df_transformed = df_clean.withColumn("total_value", col("quantity") * col("price"))

df_transformed.display()

# COMMAND ----------

# Agrupar por categoria
df_gold = (df_transformed
           .groupBy("category")
           .sum("total_value")
           .withColumnRenamed("sum(total_value)", "total_sales")
)
df_gold.display()