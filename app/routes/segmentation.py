
import os
import shutil
from PIL import Image

from fastapi import APIRouter, UploadFile, File, Query
from fastapi.responses import JSONResponse

from app.models.sam import segment_everything
from app.utils.format_data import serialize_annotations, compress_data


router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/segment-image/")
async def segment_image(
    file: UploadFile = File(...),
    input_size: int = Query(1024, ),
    better_quality: bool = Query(False, ),
    with_contours: bool = Query(True, ),
    use_retina: bool = Query(True, ),
    mask_random_color: bool = Query(True, ),
):
    """ Segment an image using the SAM model. """

    file_location = f"{UPLOAD_DIR}/{file.filename}"

    # Save uploaded image
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read the image using PIL
    image  = Image.open(file_location)

    # Segment the image using the SAM model
    annotations = segment_everything(image,
                                     input_size,
                                     better_quality,
                                     with_contours,
                                     use_retina,
                                     mask_random_color)

    # Convert NumPy arrays to lists for JSON serialization
    serialized_annotations = serialize_annotations(annotations)

    # To transmit the data faster, compress and encode it
    compressed_data = compress_data(serialized_annotations)

    return JSONResponse(content={"filename": file.filename, "compress_annotations": compressed_data})
