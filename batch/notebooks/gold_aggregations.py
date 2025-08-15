# Databricks notebook source
# Gold aggregations (placeholder)
from pyspark.sql import functions as F

# TODO: build star schema / aggregates
# sales = spark.table("retail.silver.sales_clean")
# daily = sales.groupBy("event_date","product_id").agg(F.sum("amount").alias("revenue"))
# daily.write.format("delta").mode("overwrite").saveAsTable("retail.gold.daily_sales")
