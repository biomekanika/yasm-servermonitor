#!/bin/bash

echo "YASM build and deploy"
echo "====================="

image_name="yasm-servermonitor"

echo "Getting running container ID..."
yasmid=$(docker ps | grep "$image_name" | awk '{ print $1 }')
if [ -z "$yasmid" ]; then
    echo "No running YASM container found."   
else
    echo "Found $yasmid"
    echo "Stopping container..."
    docker stop $yasmid >/dev/null 2>&1
    echo "Done."
fi

echo "Getting stopped container ID..."
yasmid=$(docker ps -f 'status=exited' | grep "$image_name" | awk '{ print $1 }')
if [ -z "$yasmid" ]; then
    echo "No stopped YASM container found."
    echo "Skipping pre-build steps..."
else
    echo "Found $yasmid"
    echo "Removing container..."
    docker container rm $yasmid >/dev/null 2>&1
    echo "Done."
fi

echo "Building Docker image from source..."
docker build -t $image_name .

echo "Deploying YASM..."
docker run -d -p 80:80 $image_name
docker ps