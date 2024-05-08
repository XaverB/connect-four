# Use an official Java 8 JDK image from the Docker Hub
FROM openjdk:8-jdk

# Set the working directory inside the container
WORKDIR /workspace

# Copy the local directory contents to the container
COPY . /workspace

# Install necessary packages for Java GUI applications
RUN apt-get update && apt-get install -y \
    x11-apps \
    libxtst6 \
    libxrender1 \
    libxi6 \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables to configure Java and X11 forwarding
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV DISPLAY host.docker.internal:0.0

# The command that runs when the container starts
CMD ["bash"]
