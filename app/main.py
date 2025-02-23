""" FastAPI application for segmenting images using the SAM model. """
from fastapi import FastAPI

from app.routes.segmentation import router as segmentation_router

app = FastAPI()

# Include segmentation route
app.include_router(segmentation_router)
