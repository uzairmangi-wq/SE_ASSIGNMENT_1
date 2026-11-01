# Task 3: Authentication and Authorization in Flask API

## Project Name
Employee Management API

## Objective
To develop a Flask API that authenticates users and restricts employee management operations according to their roles.

## Technologies Used
- Python
- Flask
- JSON
- cURL

## User Roles

| Role | Permissions |
|---|---|
| Employee | View employee records |
| Administrator | View, add, update and delete employee records |

## API Endpoints

| Method | Endpoint | Access |
|---|---|---|
| POST | `/login` | Public |
| GET | `/employees` | Employee and Administrator |
| POST | `/employees` | Administrator only |
| PUT | `/employees/<id>` | Administrator only |
| DELETE | `/employees/<id>` | Administrator only |

## Authentication
Users must log in with valid credentials to receive an authentication token. The token is sent through the `Authorization` HTTP header.

## Authorization
- Employee can only view records.
- Administrator can view, add, update and delete records.

## Security Responses
- `401 Unauthorized`: Missing or invalid authentication.
- `403 Forbidden`: Authenticated user lacks permission.
- `404 Not Found`: Employee record does not exist.

## Testing
The API is tested using cURL:
- Employee login
- Administrator login
- Employee viewing records
- Employee attempting an administrator-only operation
- Administrator adding, updating and deleting records
- Unauthenticated access
- Invalid login credentials

## Note
This is a classroom demonstration. The credentials and tokens are for testing only.
