# MobileSAM POST API

FastAPI service to deploy the MobileSam segmentation model, 
the service is containerize Docker and Docker compose, 
and ensure efficient interaction with the model on the CPU.
  
- **API Endpoints:** This Service expose a POST endpoint `/segment-image` 
it accept an image file, process it through MobileSam, and return the segmentation result.

The API return 
```
{
  "filename": "dog.jpg",
  "annotations": COMPRESS_DATA
}
```
to decompress the result you can use the funtion decompress_data() in app.utils.format_data

OR :
```
    # Decompress and check data
    decompressed_json = zlib.decompress(base64.b64decode(json_response["compress_annotations"])).decode()
```

## LAUNCH:
To Start your container use:
```sh
$ docker-compose up
```
go to http://localhost:8000/docs to try the API Endpoint

### Connect to the FastAPI container
```sh
$ docker ps
```
It will return something in the form of:
CONTAINER ID   IMAGE                        COMMAND                  CREATED         STATUS         PORTS                                       NAMES
83a64e13ae7c   task-backend-xfarm-fastapi   "uvicorn app.main:ap…"   9 minutes ago   Up 9 minutes   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   task-backend-xfarm-fastapi-1

With this command you can see the ID of the container `83a64e13ae7c` 

To have shell access to the container :
```sh
$ docker exec -it 83a64e13ae7c bash
```
### Testing.
Go inside the fastapi container as explain bellow
Run to test:
```sh
$ pytest tests/
```
