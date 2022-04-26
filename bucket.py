
import boto3

class BucketAPI:

    def list_Bucket():
        client = boto3.client('s3')
        names = [ele['Name'] for ele in client.list_buckets()['Buckets']]
        locations = [client.get_bucket_location(Bucket=ele) for ele in names]
        b = client.list_buckets()
        b['regions'] = []
        b['regions'].append(locations[0]['LocationConstraint'])
        return b

    def create_Bucket(Name,Region):
        client = boto3.client('s3')
        if Region == '':
            client.create_bucket(Bucket=Name,CreateBucketConfiguration={"LocationConstraint" : "us-east-2"})
        else:
            location = { "LocationConstraint" : Region}
            client.create_bucket(Bucket=Name,CreateBucketConfiguration=location)

    def remove_Bucket(val):
        client = boto3.client('s3')
        client.delete_bucket(Bucket=val)

    def upload_file(Name,fileName):
        client = boto3.client('s3')
        client.upload_file(fileName,Name,fileName)
