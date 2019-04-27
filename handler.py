import json
import os

import boto3

BATCH_JOB_QUEUE_ARN = os.environ.get("BATCH_JOB_QUEUE_ARN")
BATCH_JOB_DEFINITION = os.environ.get("BATCH_JOB_DEFINITION")

def batch(event, context):
    client = boto3.client('batch')
    job_name = "lambda_example_job"

    result = client.submit_job(
        jobName = job_name,
        jobQueue = BATCH_JOB_QUEUE_ARN,
        jobDefinition = BATCH_JOB_DEFINITION,
        parameters = {
            "first_arg": "hello",
            "second_arg": "world"
        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response