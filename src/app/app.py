# coding=utf-8
"""
Main file which assembles all routers into one.
"""

# Path, Query, Body, Cookie, Header
# response_model: Parameter of the decorator
#
# Input Model, Output Model, Database Model


from fastapi import FastAPI

from .routers import basic_timeseries
from starlette.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
    "http://localhost:8080"
]

app = FastAPI(
    title="Price Server",
    description="Provides a REST API to Norgate Data",
    version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(basic_timeseries.router)



