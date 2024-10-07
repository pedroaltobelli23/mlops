#!/bin/bash
echo "Build started: "
docker build --platform linux/amd64 -t aps-03-image:test .

docker tag aps-03-image:test "$URI":latest

echo "Push started: "
docker push "$URI":latest