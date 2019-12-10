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


app = FastAPI(
    title="Price Server",
    description="Provides a REST API to Norgate Data",
    version="1.0.0")

app.include_router(basic_timeseries.router)



