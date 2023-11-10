# Serverless QRCode Generator API

This QR code generator creates QR codes for URLs passed to it. It was built with AWS Lambda & a private S3 bucket, and it was served via AWS CloudFront.

# The API

**URL**: https://1zr2whunxh.execute-api.eu-west-1.amazonaws.com/default/qr-code-gen

## Testing with _curl_

curl -X POST -d '{"url": "https://test.com"}' https://1zr2whunxh.execute-api.eu-west-1.amazonaws.com/default/qr-code-gen

## Demo

https://github.com/Adeyomola/serverless-qr-code-API-AWS-Lambda/assets/44479277/7757224a-8ee1-4710-98ab-4339ceba63d0

