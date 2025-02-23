""" Utility functions for the Flask app """
import json
import zlib
import base64

def compress_data(data):
    """Compress and encode data for faster transmission"""
    json_data = json.dumps(data)  # Convert to JSON string
    compressed_data = zlib.compress(json_data.encode())  # Compress
    encoded_data = base64.b64encode(compressed_data).decode()  # Encode to Base64
    return encoded_data

def decompress_data(compressed_json):
    """Decompress Base64-encoded zlib data"""
    compressed_data = base64.b64decode(compressed_json)
    json_data = zlib.decompress(compressed_data).decode()
    return json.loads(json_data)

def serialize_annotations(annotations):
    """Convert NumPy arrays to lists for JSON serialization"""
    serialized_annotations = []
    for annotation in annotations:
        serialized_annotations.append({
            "segmentation": annotation["segmentation"].tolist(),  # Convert mask to list
            "area": annotation["area"],
            "bbox": annotation["bbox"],
            "predicted_iou": float(annotation["predicted_iou"]),
            "point_coords": annotation["point_coords"],
            "stability_score": float(annotation["stability_score"]),
            "crop_box": annotation["crop_box"],
        })
    return serialized_annotations
