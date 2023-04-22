FROM public.ecr.aws/lambda/python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY app.py .

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]