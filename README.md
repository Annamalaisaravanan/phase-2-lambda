# phase-2-lambda

## Solution Architecture

![alt text](https://github.com/Annamalaisaravanan/phase-2-lambda/blob/07e6801c32d35adc832ef504ede21d4989bd1c91/ECS-lambda3.jpg)

## Solution Workflow

### Frontend UI

1. Create an IAM Role for accessing AWS services.
2. Create a GitHub repo and AWS services using Terraform registry.
3. Create a DockerFile.
4. Push the code with DockerFile to GitHub.
5. Deploy a CI/CD Pipeline with GitHub actions.
6. Run a Docker Image with ECS Fargate.

### Backend(Model serving using FastAPI)

1. Create a FastAPI application code with handler function.
2. Create a DockerFile.
3. Create a Lambda function and upload the docker image to it.
4. Create an API Gateway endpoint to connect lambda function to the application.

## Code Execution

To run the streamlit application. Run the following command from the base directory.

``` 
streamlit run streamlit/app.py
```

To run the FastAPI in localhost. Run the following command from the base directory.

``` 
uvicorn fastapi/app:app --reload
```



