"""
FastAPI To-Do List API Starter Code

This is the skeleton of a to-do list REST API built with FastAPI.
Complete the implementation by following the assignment tasks.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# TODO: Define a Pydantic model for To-Do items
# The model should include:
# - id: integer (optional, auto-generated)
# - title: string (required)
# - description: string (optional)
# - completed: boolean (default False)


# In-memory storage for to-do items
todos = [
    {"id": 1, "title": "Learn FastAPI", "description": "Complete FastAPI fundamentals", "completed": False},
    {"id": 2, "title": "Build an API", "description": "Create a REST API with CRUD operations", "completed": False},
]

next_id = 3  # Counter for generating new IDs


# Task 1: Implement GET endpoints
@app.get("/todos/")
async def get_all_todos():
    """
    TODO: Implement this endpoint to return all to-do items.
    Return the entire todos list.
    """
    pass


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    """
    TODO: Implement this endpoint to return a specific to-do item by ID.
    If the item doesn't exist, raise an HTTPException with status code 404.
    """
    pass


# Task 2: Implement POST endpoint
@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo):
    """
    TODO: Implement this endpoint to create a new to-do item.
    - Accept a to-do object in the request body
    - Generate a unique ID for the item
    - Add it to the todos list
    - Return the created item with status code 201
    """
    pass


# Task 3 & 4: Implement PUT and DELETE endpoints
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, updated_todo):
    """
    TODO: Implement this endpoint to update an existing to-do item.
    - Find the item by ID
    - Update its fields with the new values
    - Return the updated item
    - Return 404 if the item doesn't exist
    """
    pass


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    """
    TODO: Implement this endpoint to delete a to-do item by ID.
    - Remove the item from the todos list
    - Return 204 No Content on success
    - Return 404 if the item doesn't exist
    """
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
