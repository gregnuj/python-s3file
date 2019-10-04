#!/usr/bin/env python

import os
import boto3
import argparse
from botocore.exceptions import NoCredentialsError


evars = {}
for evar in ['S3_BUCKET', 'S3_ACCESS', 'S3_SECRET']:
   if evar in os.environ.keys():
      evars[evar] = os.environ[evar]
   else:
      evars[evar] = False


def s3Upload(local_file, bucket, s3AccessKey, s3SecretKey):
    s3 = boto3.client('s3', aws_access_key_id=s3AccessKey, aws_secret_access_key=s3SecretKey)
    s3_file = os.path.basename(local_file)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False

def s3Download(local_file, bucket, s3AccessKey, s3SecretKey):
    s3 = boto3.client('s3', aws_access_key_id=s3AccessKey, aws_secret_access_key=s3SecretKey)
    s3_file = os.path.basename(local_file)

    try:
        s3.download_file(bucket, s3_file, local_file)
        print("Download Successful")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--upload', action='store', default =False)
    group.add_argument('-d', '--download', action='store', default=False)
    parser.add_argument('-b', '--bucket', action='store', default=evars['S3_BUCKET'])
    parser.add_argument('-a', '--access', action='store', default=evars['S3_ACCESS'])
    parser.add_argument('-s', '--secret', action='store', default=evars['S3_SECRET'])
    args = parser.parse_args()
    if args.upload:
        uploaded = s3Upload(args.upload, args.bucket, args.access, args.secret)
    elif args.download:
        downloaded = s3Download(args.download, args.bucket, args.access, args.secret)

