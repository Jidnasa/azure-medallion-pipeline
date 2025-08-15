# Databricks notebook source
# Silver transformations (placeholder)
from pyspark.sql import functions as F

# TODO: read bronze tables, cleanse/standardize, write to silver
# df = spark.table("retail.bronze.sales")
# df_clean = df.dropna(subset=["ProductId"]).withColumn("event_date", F.to_date("timestamp"))
# df_clean.write.format("delta").mode("overwrite").saveAsTable("retail.silver.sales_clean")
