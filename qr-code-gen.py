import json
import qrcode
import io
import boto3

s3 = boto3.client('s3')

def qr_gen(event, context):
    body = json.loads(event['body']) # converts event['body'] json to deserialized object in Python
    url = body['url']

    qr_img = qrcode.make(url) # create QR code
    qr_img_byte = io.BytesIO() # initialize a file-like object operating on bytes data in memory
    qr_img.save(qr_img_byte) # save the QR code with the name qr_img_byte
    qr_img_byte = qr_img_byte.getvalue() # returns bytes containing the contents of the buffer (QR code saved as qr_img_byte in step2)

    filename = url.split("://")[1].replace('/', '_') + ".png" # splits url into http(s) and rest of URL; uses rest of URL as filename while replace slashes with underscores

    s3.put_object(Bucket='qr-code-gen', Key=filename, Body=qr_img_byte, ContentType='image/png', ACL='public-read') # put QR code in S3 bucket

    # Generate URL for the QR code we put in an S3 bucket
    location = s3.get_bucket_location(Bucket='qr-code-gen')['LocationConstraint']
    region = '' if location is None else f'{location}'
    qr_code_url = f"https://s3-{region}.amazonaws.com/qr-code-gen/{filename}"

    return {
        'isBase64Encoded': 'false',
        'statusCode': 200,
        'headers': {"Content-Type": "application/json"},
        'body': json.dumps({'message': 'QR Code successfully generated', 'qr_code_url': qr_code_url})
    }

