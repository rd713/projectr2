# api/index.py

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum  # Required for serverless handler

from app.main import router as app_router  # Import your logic

app = FastAPI()
app.include_router(app_router)

handler = Mangum(app)  # 👈 for Vercel to run FastAPI
