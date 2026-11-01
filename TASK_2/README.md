# Task 2: API Key Generation and Sharing

## Project Name
RootSoftware Text Processing API

## Objective
To develop a Flask API that processes text using API keys for authentication.

## Technologies Used
- Python
- Flask
- JSON
- cURL
- Python Secrets Module

## API Endpoint
`POST /process`

## API Features
1. Generates three unique API keys for three consumers.
2. Accepts API keys through the `X-API-Key` HTTP header.
3. Validates API keys before processing requests.
4. Converts submitted text into uppercase.
5. Rejects invalid or missing API keys with HTTP 401.
6. Rejects requests with missing text using HTTP 400.

## Sample Request
- Method: POST
- URL: `http://127.0.0.1:5001/process`
- Header: `Content-Type: application/json`
- Header: `X-API-Key: YOUR_API_KEY`
- JSON Body: `{"text":"hello rootsoftware"}`

## Expected Response
`{"processed_text":"HELLO ROOTSOFTWARE"}`

## Testing
The API is tested using cURL with:
- Consumer 1 valid key
- Consumer 2 valid key
- Consumer 3 valid key
- Invalid API key
- Missing API key
- Missing text

## Security
API keys should not be uploaded to public repositories or exposed in screenshots.
