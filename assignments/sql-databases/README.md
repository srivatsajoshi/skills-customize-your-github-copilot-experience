# 📘 Assignment: SQL & Relational Databases

## 🎯 Objective

Learn to design, create, and query relational databases using SQL. Build a student management system with multiple tables, then write Python code to interact with the database using structured queries.

## 📝 Tasks

### 🛠️ Task 1: Design and Create a Relational Database Schema

#### Description
Create a SQLite database with multiple related tables for a school system. You'll design tables for students, courses, and enrollments, establishing relationships between them.

#### Requirements
Your database should:

- Create a `students` table with columns: `student_id` (primary key), `name`, `email`, `grade_level`, and `enrollment_date`
- Create a `courses` table with columns: `course_id` (primary key), `course_name`, `instructor`, `credits`, and `description`
- Create an `enrollments` table with columns: `enrollment_id` (primary key), `student_id` (foreign key), `course_id` (foreign key), `enrollment_date`, and `grade`
- Define appropriate primary keys and foreign key relationships
- Successfully execute the schema creation without errors


### 🛠️ Task 2: Insert and Query Data

#### Description
Populate your database with sample data and practice retrieving information using various SQL queries.

#### Requirements
Your solution should:

- Insert at least 5 students with realistic data
- Insert at least 4 courses with varied credit values
- Create at least 8 enrollment records linking students to courses
- Write queries to: list all students, show all courses, retrieve a student's enrolled courses with grades, and count total enrollments
- Execute all queries successfully and verify the results


### 🛠️ Task 3: Implement Python Database Operations

#### Description
Write a Python program that connects to your SQLite database and provides functions to perform CRUD operations (Create, Read, Update, Delete).

#### Requirements
Your Python program should:

- Connect to the SQLite database using the `sqlite3` module
- Implement a function to add a new student to the database
- Implement a function to retrieve and display all students
- Implement a function to update a student's grade in a specific course
- Implement a function to delete an enrollment record
- Include error handling for invalid operations
- Demonstrate all functions with sample operations


### 🛠️ Task 4: Write Advanced Queries

#### Description
Create SQL queries that combine multiple tables and use aggregation functions to extract meaningful insights from your database.

#### Requirements
Your queries should:

- Use `JOIN` statements to combine data from multiple tables
- Calculate the average grade per course using `GROUP BY` and `AVG()`
- Find students enrolled in more than one course
- List courses with the most enrollments
- Write at least one query using `WHERE` with multiple conditions
- Document each query with a comment explaining what it retrieves
