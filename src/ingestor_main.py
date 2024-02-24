from os import path
import logging
import uvicorn
from fastapi import FastAPI

import src.config as config
from src.config import Settings

config.settings = Settings('../.env')

from src.app import router as app_router
from src.driver import router as driver_router

app = FastAPI()

settings = config.settings

app.include_router(app_router.router)
app.include_router(driver_router.router, prefix="/driver")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
