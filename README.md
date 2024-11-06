# To-Do Application using AWS Lambda, API Gateway and DynamoDB

This project is a simple To-Do application that uses AWS Lambda, API Gateway, and DynamoDB for the backend. It supports creating, reading, updating, and deleting (CRUD) todo items through RESTful API calls.

## Project Structure

- **Backend**: AWS Lambda functions with API Gateway and DynamoDB
---

## Table of Contents

1. [Backend Setup](#backend-setup)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)

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

4. **Deploy the API**

   - Deploy the API in API Gateway to a stage (e.g., `dev`).
   - Note the base URL of the deployed API.

## Example Lambda Function Code

The Lambda function code for creating, reading, updating, and deleting todos is provided in this repository.

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

