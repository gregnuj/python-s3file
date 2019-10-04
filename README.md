# python-s3file
upload or download to s3 bucket using python

# git repo
git clone https://github.com/gregnuj/python-s3file.git
cd python-s3file

## use providing bucket info via command line

```
python s3file.py -u test.txt --bucket 'XXXXXXXXXXX' --access 'XXXXXXXXXXX' --secret 'XXXXXXXXXXX'
Upload Successful

python s3file.py -d test.txt --bucket 'XXXXXXXXXXX' --access 'XXXXXXXXXXX' --secret 'XXXXXXXXXXX'
Download Successful
```

## use providing bucket info via env vars

```
export S3_BUCKET="XXXXXXXXXXX"
export S3_ACCESS="XXXXXXXXXXXXXXXXXXXXXX"
export S3_SECRET="XXXXXXXXXXX"

python s3file.py --upload test.txt
Upload Successful

python s3file.py --download test.txt
Download Successful
```
