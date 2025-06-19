import boto3
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv("include/config.env")

def upload_to_s3():
    try:
        # Load AWS credentials
        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        bucket_name = os.getenv("AWS_BUCKET_NAME")

        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        local_file = "data/covid_countries_data.csv"
        s3_key = "raw_data/covid_countries_data.csv"  #	path inside your bucket

        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded '{local_file}' to 's3://{bucket_name}/{s3_key}'")

    except Exception as e:
        print(f"Failed to upload to S3: {e}")


if __name__ == "__main__":
    upload_to_s3()

=======
import boto3
import os
from dotenv import load_dotenv

# Load credentials from .env
load_dotenv("include/config.env")

def upload_to_s3():
    try:
        # Load AWS credentials
        aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        bucket_name = os.getenv("AWS_BUCKET_NAME")

        s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        local_file = "data/covid_countries_data.csv"
        s3_key = "raw_data/covid_countries_data.csv"  #	path inside your bucket

        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded '{local_file}' to 's3://{bucket_name}/{s3_key}'")

    except Exception as e:
        print(f"Failed to upload to S3: {e}")


if __name__ == "__main__":
    upload_to_s3()
