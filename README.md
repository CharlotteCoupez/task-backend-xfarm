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






Evaluation will be based on the following criteria:
- Ability to use FastAPI to create a microservice.
- Ability to create a project structure that is clean and easy to understand.
- Ability to make the project ready for production.
- Ability to use Docker to containerize the service.
- Ability to use the MobileSam segmentation model.
- Ability to create a RESTful API that allows users to interact with the model.

## Additional informations

- As long as the mandatory criteria are met, you can use any additional libraries you want.

## Task Overview

**Title:** MobileSam Segmentation Model Service

**Expected Time to Complete:** 1-4 hours

**Objective:** Develop a FastAPI service to deploy the MobileSam segmentation model, containerize the service with Docker, and ensure efficient interaction with the model on the CPU.

**Background:**
MobileSam is a machine learning model specialized in image segmentation on CPUs. Your task is to create a microservice that allows users to interact with this model via an API.

## Task Description

- **Develop a Microservice:** Use Python FastAPI framework to expose the MobileSam segmentation model as a RESTful API.
  
- **Model Integration:** Incorporate the MobileSam segmentation model into your service. It should process image inputs and return segmentation results.
