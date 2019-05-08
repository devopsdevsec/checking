import boto3
s3 = boto3.resource('s3')

for buket in s3.bukets.all():
    print(buket.name)
