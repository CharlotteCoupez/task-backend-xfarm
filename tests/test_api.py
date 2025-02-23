from fastapi.testclient import TestClient

from app.main import app
from app.utils.format_data import decompress_data

client = TestClient(app)  # Initialize test client

def test_segment_image():
    """Test the segmentation endpoint with an image."""

    file_location = "resources/dog.jpg"

    # Open the image and convert to byte stream
    with open(file_location, "rb") as file:
        image_bytes = file.read()

    # Send POST request with multipart/form-data
    response = client.post(
        "/segment-image/",
        files={"file": ("dog.jpg", image_bytes, "image/jpeg")},
        params={  # Query parameters
            "input_size": 1024,
            "better_quality": False,
            "with_contours": True,
            "use_retina": True,
            "mask_random_color": True
        }
    )
    assert response.status_code == 200  # Ensure the request was successful
    json_response = response.json()

    assert "filename" in json_response  # Ensure filename exist
    assert "compress_annotations" in json_response  # Ensure annotations exist

    # Decompress and verify JSON format
    compressed_data = json_response["compress_annotations"]
    decompressed_json = decompress_data(compressed_data)

    # Ensure the decompressed data is a list
    assert isinstance(decompressed_json, list)

    # Ensure all keys are present (here for the first annotation)
    assert "segmentation" in decompressed_json[0].keys()
    assert "area" in decompressed_json[0].keys()
    assert "bbox" in decompressed_json[0].keys()
    assert "predicted_iou" in decompressed_json[0].keys()
    assert "point_coords" in decompressed_json[0].keys()
    assert "stability_score" in decompressed_json[0].keys()
    assert "crop_box" in decompressed_json[0].keys()

    # Ensure the data types are correct
    assert isinstance(decompressed_json[0]['segmentation'], list)
    assert isinstance(decompressed_json[0]['area'], int)
    assert isinstance(decompressed_json[0]['bbox'], list)
    assert isinstance(decompressed_json[0]['predicted_iou'], float)
    assert isinstance(decompressed_json[0]['point_coords'], list)
    assert isinstance(decompressed_json[0]['stability_score'], float)
    assert isinstance(decompressed_json[0]['crop_box'], list)

    print("✅ Test Passed!")
