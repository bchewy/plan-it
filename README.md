# Plan-IT

This project consists of two main components: the backend and the frontend. Below are the instructions for setting up and running each component in both development and production environments.

## Backend Setup and Running Instructions

### Development Environment

1. Navigate to the `backend` directory.
2. Run the Flask application using the default development server.
    ```bash
    flask run
    ```

### Production Environment

1. Navigate to the `backend` directory.
2. Run the application using Gunicorn as the WSGI server. The following command will start Gunicorn with 4 worker processes and bind it to all available network interfaces on port 8888.
    ```bash
    gunicorn -w 4 -b 0.0.0.0:8888 app:app
    ```

## Frontend Setup and Running Instructions

### Development Environment

1. Navigate to the `frontend` directory.
2. Run the following command to start the development server:
    ```bash
    npm install --legacy-peer-deps
    npm run dev #to start dev server
    ```
