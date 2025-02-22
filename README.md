# Take Home Assignment - Software Engineer

This assignment is designed to assess your software engineering skills in the context of integrating and deploying a machine learning model.

Evaluation will be based on the following criteria:
- Ability to use FastAPI to create a microservice.
- Ability to create a project structure that is clean and easy to understand.
- Ability to make the project ready for production.
- Ability to use Docker to containerize the service.
- Ability to use the MobileSam segmentation model.
- Ability to create a RESTful API that allows users to interact with the model.

## Mandatory:
- You have to use FastAPI to create the microservice.
- You have to use Docker to containerize the service.
- Code should be easy to test for the reviewer.

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
  
- **API Endpoints:** Create a POST endpoint `/segment-image` to accept an image file, process it through MobileSam, and return the segmentation result.
  
- **Documentation:** Provide clear instructions for setting up, running, and interacting with the service in a README.md file.


## Submission

- Submit your code via a GitHub/Gitlab repository link.
- Include a README file with detailed setup and usage instructions.
- Provide any necessary scripts or files for testing the API.
