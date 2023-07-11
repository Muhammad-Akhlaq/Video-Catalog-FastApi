# -*- coding: utf-8 -*-
from typing import Dict
from core.logger import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.routes import add_routes
from db.database import engine

app = FastAPI(openapi_url="/openapi.json", title="Video-Catalog-FastApi")

add_routes(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping", tags=["Health"])
async def read_root() -> Dict:
    return {"message": "pong"}


@app.on_event("shutdown")
async def shutdown_event():
    try:
        await engine.dispose()
    except Exception as e:
        logger.warning(f"engine dispose failed with following error: {str(e)}")
    finally:
        logger.info("engine disposed successfully")
