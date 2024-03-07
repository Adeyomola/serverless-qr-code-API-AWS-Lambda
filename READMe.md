# Serverless QRCode Generator API Documentation

## Introduction
The QR Code Generator API allows users to generate QR codes from provided URLs and store them in an Amazon S3 bucket. This documentation provides instructions on how to interact with the API, including authentication, available endpoints, request/response formats, and sample code snippets.

## The API

**URL**: https://1zr2whunxh.execute-api.eu-west-1.amazonaws.com/default/qr-code-gen

## Authentication
No authentication is required to use this API.

## Endpoints
### Generate QR Code
Generates a QR code from a provided URL and stores it in an Amazon S3 bucket.

- Endpoint: `/qr_gen`
- HTTP Method: POST
- Request Body Parameters:
  - `url` (string): The URL to encode into the QR code.
- Response:
  - `statusCode` (int): HTTP status code indicating the success of the request (200 for success).
  - `headers` (object): HTTP headers.
  - `body` (string): JSON-formatted response containing the following fields:
    - `message` (string): Success message.
    - `qr_code_url` (string): URL to access the generated QR code image.

## Sample Request

```
curl -X POST -d '{"url": "https://test.com"}' \
https://1zr2whunxh.execute-api.eu-west-1.amazonaws.com/default/qr-code-gen
```

## Demo

https://github.com/Adeyomola/serverless-qr-code-API-AWS-Lambda/assets/44479277/7757224a-8ee1-4710-98ab-4339ceba63d0

## Error Handling
In case of errors, the API will return an appropriate HTTP status code along with an error message in the response body.

## Rate Limiting and Throttling
There are no rate limiting or throttling restrictions imposed by the API.

## Best Practices and Tips
- Ensure that the provided URL is valid and properly formatted.
- Handle any potential errors returned by the API, such as network issues or invalid input.

