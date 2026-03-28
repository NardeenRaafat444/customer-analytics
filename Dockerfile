# Use official Python image
FROM python:3.10-slim
#Uses Python environment, base image.
#docker pull python:3.11

# Install required libraries
RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests


# Set working directory, This tells Docker that inside the container, the main folder you will work from is:
WORKDIR /app/pipeline/
#Creates working folder inside container.
#Inside the container, treat /app/pipeline as the current working folder.   like doing cd automatically
#Because your project has multiple files: You need one predictable folder inside the container where all these files live.


# Copy project files into container
COPY . /app/pipeline/
#Take everything in my current project folder on the host machine and copy it into /app/pipeline/ inside the image/container.

# Install required libraries
RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

# Start an interactive bash shell when the container runs
#CMD ["bash"] : This changes Docker from: Interactive mode to:Fully automated mode
CMD ["bash", "run_pipeline.sh"]

#From the Docker lab, an image is a template of layers used to create a container.
#an image is a saved blueprint
#a container is a running A container is the running app environment created from an image.
#a container runs a process, and if that process stops, the container stops

#the Dockerfile helps build the image
#the image contains Python + packages + your files
#when you run the image, Docker creates a container
#the container is where your pipeline actually executes


#the final dot means:
#use the current folder as the build context

#steps to run in terminal
#1) Build the Docker image from dockerfile : docker build -t customer-analytics
#You create your own custom image, Docker builds it using instructions from your Dockerfile

#2) Run the container: docker run -it --name mypipeline customer-analytics

#3) we are inside the container now , inside the working directory : ls

#4) Run the pipeline manually inside the container:: python ingest.py marketing_campaign.csv: 

#5) bash summary.sh