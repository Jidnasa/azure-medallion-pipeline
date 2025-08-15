# Databricks notebook source
# Bronze ingestion (placeholder)
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
# TODO: read from ADLS Gen2 raw path and enforce schema
# df = spark.read.format("csv").option("header","true").load("abfss://.../bronze/...")
# df.write.format("delta").mode("append").saveAsTable("retail.bronze.sales")
