import boto3
from botocore.client import Config
import zipfile

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

build_bucket = s3.Bucket('cloudbuild.jbarnardportfolio.com')
portfolio_bucket = s3.Bucket('cloud.jbarnardportfolio.com')

build_bucket.download_file('portfolio.zip', '/tmp/portfolio.zip')

with zipfile.ZipFile('/tmp/portfolio.zip') as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        target_bucket.upload_fileobj(obj, nm)
        target_bucket.Object(nm).Acl().put(ACL='public-read')
