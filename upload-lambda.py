import boto3
from botocore.client import Config
import BytesIO
import zipfile

s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

portfolio_bucket = s3.Bucket('cloud.jbarnardportfolio.com')
build_bucket = s3.Bucket('cloudbuild.jbarnardportfolio.com')

portfolio_zip = io.BytesIO()
build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj, nm)
        portfolio_bucket.Object(nm).ACL().put(ACL='public-read')
