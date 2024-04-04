# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org Flask

# Make port 5000 available to the world outside this container
EXPOSE 5000/udp
EXPOSE 5000/tcp
EXPOSE 37020/udp

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "flask_node.py"]
