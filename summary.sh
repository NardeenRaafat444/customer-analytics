#!/bin/bash

echo "Copying results from container..."

# Create results folder on host
mkdir -p results

# Copy files from container to host
docker cp mypipeline:/app/pipeline/insight1.txt results/
docker cp mypipeline:/app/pipeline/insight2.txt results/
docker cp mypipeline:/app/pipeline/insight3.txt results/
docker cp mypipeline:/app/pipeline/summary_plot.png results/
docker cp mypipeline:/app/pipeline/clusters.txt results/

echo "Files copied successfully."

# Stop container
docker stop mypipeline

# Remove container
docker rm mypipeline

echo "Container stopped and removed."
#This is just a list of bash commands.

#🧠 Where is bash used in your project?: CMD ["bash"] : Start bash shell when container runs