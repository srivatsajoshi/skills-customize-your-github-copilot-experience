# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you'll learn how to build a RESTful API using the FastAPI framework. You'll create endpoints to handle different HTTP methods, implement request validation with Pydantic models, and handle errors gracefully. By the end, you'll have a functioning API that can receive, process, and respond to client requests.

## 📝 Tasks

### 🛠️ Task 1: Create a Basic FastAPI Application with GET Endpoints

#### Description
Create a FastAPI application that serves as a simple to-do list API. Start by creating a basic structure with at least two GET endpoints: one that returns all to-do items and another that retrieves a specific item by ID.

#### Requirements
Your application should:

- Initialize a FastAPI application instance
- Define at least two GET endpoints (`/todos/` and `/todos/{id}`)
- Return sample to-do items as JSON responses
- Use path parameters to retrieve items by ID
- Include proper HTTP status codes (200 for success)

### 🛠️ Task 2: Add POST Endpoints to Create Resources

#### Description
Extend your API by adding the ability to create new to-do items. Implement a POST endpoint that accepts item data from clients and stores it in memory (using a list or dictionary).

#### Requirements
Your application should:

- Define a POST endpoint (`/todos/`) that accepts JSON data
- Create a Pydantic model to validate incoming request data
- Add the new item to your in-memory storage
- Return the newly created item with a 201 status code
- Ensure the endpoint accepts required fields (e.g., title, description)

### 🛠️ Task 3: Implement Request Validation and Error Handling

#### Description
Improve your API's robustness by adding input validation and proper error responses. Use Pydantic models to validate request data and return meaningful error messages when validation fails.

#### Requirements
Your application should:

- Use Pydantic models with type hints and field validation
- Return 400 status code for invalid requests
- Return 404 status code when a to-do item is not found
- Include error messages that explain what went wrong
- Handle edge cases like empty titles or negative IDs

### 🛠️ Task 4 (Stretch): Add Update and Delete Operations

#### Description
Enhance your API with full CRUD operations by implementing PUT and DELETE endpoints. Allow users to update existing to-do items and remove items from the list.

#### Requirements
Your application should:

- Define a PUT endpoint to update existing items
- Define a DELETE endpoint to remove items
- Return 204 (No Content) status code for successful deletions
- Validate that items exist before updating or deleting
- Prevent invalid updates (e.g., empty titles)
