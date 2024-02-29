from typing import List
import json
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse
from datetime import datetime
from functional import seq
from pydantic import BaseModel, Field
from pyspark.sql import SparkSession
import uuid
import os
import pathlib

from src.driver.models import Pipeline

router = APIRouter()


@router.post("/start/{pipeline_id}")
async def start(pipeline_id: str) -> str:
    spark = (SparkSession.builder
             .master("local[1]")
             .appName("PySpark Tutorial")
             .getOrCreate())

    df = spark.read.format("csv").option("header", True).load("../data/example-source.csv")
    # df.printSchema()

    path = f"../data/target/{str(uuid.uuid4().hex)}"
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)
    df.toPandas().to_csv(f"{path}/example-target.csv", header=True, index=False)

    print(f'--- {spark.sparkContext.applicationId} ---')
    print(f'--- {spark.sparkContext.appName} ---')
    print("Spark version: ", spark.version)

    return ""


@router.get("/stop/{pipeline_id}")
async def stop(pipeline_id: str) -> str:
    return "stop " + pipeline_id


@router.post("/test/{pipeline_id}")
async def start(pipeline_id: str, pipeline: Pipeline) -> dict:
    result = {"id": pipeline_id, "pipeline": pipeline}
    return result
