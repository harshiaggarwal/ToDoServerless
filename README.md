# To-Do Application using AWS Lambda, API Gateway, DynamoDB, and a Simple Frontend

This project is a simple To-Do application that uses AWS Lambda, API Gateway, and DynamoDB for the backend, with a basic frontend interface. It supports creating, reading, updating, and deleting (CRUD) todo items through RESTful API calls.

## Project Structure

- **Backend**: AWS Lambda functions with API Gateway and DynamoDB
- **Frontend**: Basic HTML, CSS, and JavaScript interface for interacting with the backend

---

## Table of Contents

1. [Backend Setup](#backend-setup)
2. [Frontend Setup](#frontend-setup)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)

---

# Backend Setup

## Requirements

- AWS Account
- Node.js and npm (for local development and testing)
- AWS CLI (for deployment and testing)

## Step-by-Step Guide

1. **Create DynamoDB Table**

   - Name: `ToDoTable`
   - Primary Key: `id` (String)

2. **Create Lambda Functions**

   - **Create Todo**: Adds a new item to the DynamoDB table.
   - **Get All Todos**: Retrieves all todo items.
   - **Update Todo**: Updates the status of a todo item.
   - **Delete Todo**: Deletes a todo item by ID.

   Each Lambda function should have a policy allowing access to `ToDoTable`.

3. **Set Up API Gateway**

   - Create a new API in API Gateway (REST API).
   - Set up routes and link each HTTP method (POST, GET, PUT, DELETE) to the corresponding Lambda function.
   - Enable CORS on each endpoint for frontend communication.

4. **Deploy the API**

   - Deploy the API in API Gateway to a stage (e.g., `dev`).
   - Note the base URL of the deployed API (you’ll use this in the frontend).

## Example Lambda Function Code

The Lambda function code for creating, reading, updating, and deleting todos is provided in this repository.

# Frontend Setup

## Project Structure


## Steps

1. Clone this repository or download the frontend files.
2. Open `script.js` and update the `apiUrl` variable with your API Gateway URL (e.g., `https://YOUR_API_ID.execute-api.YOUR_REGION.amazonaws.com/prod/todos`).
3. Open `index.html` in a web browser to interact with your Todo API.

# Usage

## Commands

- **Create Todo**: Enter an ID and status, then click "Create Todo."
- **Get All Todos**: Click "Get All Todos" to display all tasks.
- **Update Todo**: Enter an ID and new status, then click "Update Todo."
- **Delete Todo**: Enter an ID, then click "Delete Todo."

# API Endpoints

1. **Create Todo**
   - **Method**: `POST`
   - **Endpoint**: `/todos`
   - **Body**:
     ```json
     {
       "id": "string",
       "status": "string"
     }
     ```

2. **Get All Todos**
   - **Method**: `GET`
   - **Endpoint**: `/todos`

3. **Update Todo**
   - **Method**: `PUT`
   - **Endpoint**: `/todos/{id}`
   - **Body**:
     ```json
     {
       "status": "string"
     }
     ```

4. **Delete Todo**
   - **Method**: `DELETE`
   - **Endpoint**: `/todos/{id}`

---

# Future Improvements

- Add authentication with AWS Cognito.
- Create a more sophisticated frontend with frameworks like React or Vue.
- Add input validation and error handling for a better user experience.

---

