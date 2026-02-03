import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'cloud-file-storage-system-s3'

def upload_file(file):
    s3.upload_fileobj(file, BUCKET_NAME, file.name)

def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    files = []
    for obj in response['Contents']:
        print(obj)
        files.append(obj['Key'])
    return files

def download_file(file):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=file)
    return response['Body'].read()

def delete_file(filename):
    s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
    return f"{filename} deleted successfully"

