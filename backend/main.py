from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routes.users import router as users_router
from routes.opportunities import router as opportunities_router
from routes.updates import router as updates_router
from routes.schemes import router as schemes_router
from routes.recommendations import (
    router as recommendations_router
)


# Create database tables
Base.metadata.create_all(
    bind=engine
)


# Create FastAPI application
app = FastAPI(
    title="YojanaSetu AI Backend",
    description=(
        "AI-powered government scheme discovery "
        "and recommendation backend."
    ),
    version="1.0.0"
)


# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Register routes
app.include_router(
    users_router
)
app.include_router(opportunities_router)

app.include_router(updates_router)

app.include_router(
    schemes_router
)

app.include_router(
    recommendations_router
)


@app.get("/")
def home():

    return {
        "message": "YojanaSetu AI backend is running",
        "status": "success"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }