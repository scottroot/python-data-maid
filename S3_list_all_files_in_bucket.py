import boto3
import json

session = boto3.Session() # aws_access_key_id='<your_access_key_id>', aws_secret_access_key='<your_secret_access_key>')


s3 = session.resource('s3')
my_bucket = s3.Bucket('permaweb-img')

results = {}

for my_bucket_object in my_bucket.objects.all():
    # print(my_bucket_object.key)

    i = my_bucket_object.key
    ext = i.split(".")[-1]
    if ext in results:
        try:
            results[ext].append(i)
        except:
            results[ext] = [i]
    else:
        results[ext] = [i]

print(json.dumps(results, indent=4))
