# Use an official Java runtime as a parent image
FROM openjdk:11-jdk

# Set the working directory to /workspace
WORKDIR /workspace

# Copy the current directory contents into the container at /workspace
COPY . /workspace

# Install any needed packages specified in requirements.txt
# RUN apt-get update && apt-get install -y maven

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Define environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Run app when the container launches
CMD ["appletviewer", "c4.html"]
