from fastapi import FastAPI
from routers import forms
import models
from database import engine

# Create all tables (only runs if tables don't exist)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="RailOps API",
    description="Handles form submissions like wheel-specifications and bogie-checksheet",
    version="1.0.0"
)

# Include your API routes
app.include_router(forms.router)

# Optional: allows running the app with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
