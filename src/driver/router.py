from typing import List
import json
from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import StreamingResponse
from datetime import datetime
from functional import seq

router = APIRouter()


@router.get("/start/{pipeline_id}")
async def start(pipeline_id: str) -> str:
    return "start " + pipeline_id


@router.get("/stop/{pipeline_id}")
async def stop(pipeline_id: str) -> str:
    return "stop " + pipeline_id
