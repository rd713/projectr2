# api/index.py

from app.main import app as app_router

# Vercel will detect `app` as the FastAPI instance
app = app_router
