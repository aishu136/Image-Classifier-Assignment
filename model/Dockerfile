# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest

# Set the working directory to /model
WORKDIR /model

# Copy the current directory contents into the container at /model
COPY . /model

# Define environment variable for TF_CPP_MIN_LOG_LEVEL
ENV TF_CPP_MIN_LOG_LEVEL=3

# Run mnist_model.py when the container launches
CMD ["python", "model.py"]

