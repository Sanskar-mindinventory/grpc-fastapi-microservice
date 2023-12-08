import os
import logging
from fastapi import FastAPI

from src.routes.route import router

app = FastAPI(description='Resume Parser and Matcher with Job Description', title='Resume Parser Clone', version='1.1.1')

# Add route for APIs
app.include_router(router)

@app.get("/")
async def index():
    return "User Auth Service is running."
