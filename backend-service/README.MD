## Backend Service

This service is built using Python and Flask.

### API Endpoints
- `POST /print`: Prints a message.
    - **Usage:**
        ```sh
        curl -X POST http://localhost:5000/print -d "message=Hello, World!"
        ```

- `GET /add`: Adds two numbers.
    - **Usage:**
        ```sh
        curl "http://localhost:5000/add?num1=5&num2=10"
        ```

- `GET /user/{user_id}`: Retrieves a specific user by ID from fake_user_db variable in `/backend-service/src/api/routes.py`.
    - **Usage:**
        ```sh
        curl http://localhost:5000/user/1
        ```

- `GET /config`: Retrieves configuration values set by environment variables (check `/backend-service/src/api/config.py`).
    - **Usage:**
        ```sh
        curl http://localhost:5000/config
        ```

- `GET /health`: Checks the health of all routes.
    - **Usage:**
        ```sh
        curl http://localhost:5000/health
        ```

### Environment Variables
> **Note:** This is a dummy env variables list which will be printed in frontend with `/config` API to check values.
- `LOGGING_LEVEL`: The logging level for the application (default: `INFO`).
- `COUNT_VALUE`: A count value used in the application (default: `0`).
- `USER_NAME`: The username for the application (default: `default`).

## Running Tests

The test files are located in the `backend-service/src/test/` directory.

To run the tests for the backend service, use the following command:
```sh
pytest
```