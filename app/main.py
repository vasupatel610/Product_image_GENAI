"""
FastAPI application entry point for image generation service.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import image_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered image generation and editing service using Google Gemini",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include routers
app.include_router(image_router, prefix="/api/v1", tags=["images"])


@app.get("/")
async def root():
    """Root endpoint - health check"""
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.VERSION
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}
