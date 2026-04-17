import boto3
from app.utils.config import AWS_REGION, S3_BUCKET_NAME

s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(file_obj, file_name: str):
    s3_client.upload_fileobj(file_obj, S3_BUCKET_NAME, file_name)
    return {
        "bucket": S3_BUCKET_NAME,
        "key": file_name
    }