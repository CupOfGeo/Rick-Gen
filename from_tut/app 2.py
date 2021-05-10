import json
import boto3
import numpy as np
import gpt_2_simple as gpt2


#imagenet_labels= np.array(open('model/ImageNetLabels.txt').read().splitlines())
s3 = boto3.resource('s3')

def lambda_handler(event, context):
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  key = event['Records'][0]['s3']['object']['key']

  #img = readImageFromBucket(key, bucket_name).resize(IMAGE_SHAPE)
  pre = 'hi'
  out = generate_out(pre)

  print('ImageName: {0}, Prediction: {1}'.format(pre, out))

def readImageFromBucket(key, bucket_name):
  bucket = s3.Bucket(bucket_name)
  object = bucket.Object(key)
  response = object.get()
  return Image.open(response['Body'])

def generate_out(pre):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')
    My_gen = gpt2.generate(sess,
                           length=200,
                           temperature=.7,
                           prefix=pre,
                           nsamples=1,
                           batch_size=1,
                           return_as_list=True,
                           )

    return My_gen[0]