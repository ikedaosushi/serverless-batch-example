#!/bin/bash

# Variables
IMAGE=serverless-batch-example
TAG=latest
DOCKERFILE=app.dockerfile
## さっきメモしたrepositoryUriを貼り付け
ECR_URI=xxxxxxxxxx.dkr.ecr.ap-northeast-1.amazonaws.com/serverless-batch-example

# Build image
docker build -t "${IMAGE}:${TAG}" -f "${DOCKERFILE}" .

# Docker login
$(aws ecr get-login --no-include-email --region ap-northeast-1)

# Tag that image
docker tag "${IMAGE}:${TAG}" "${ECR_URI}:${TAG}"

# Push
docker push "${ECR_URI}:${TAG}"