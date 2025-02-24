import requests
import base64
import zlib

URL = 'http://localhost:8000/segment-image/'
files = {'file': open('resources/dog.jpg', 'rb')}
response = requests.post(URL, files=files)

json_response = response.json()
decompressed_json = zlib.decompress(base64.b64decode(
    json_response["compress_annotations"])).decode()

print('decompressed_json:', decompressed_json)
print('len decompressed_json:', len(decompressed_json))

