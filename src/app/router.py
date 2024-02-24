from fastapi import APIRouter
import src.config as config

router = APIRouter()
settings = config.settings


@router.get("/ping")
def ping():
    return 'pong!'
