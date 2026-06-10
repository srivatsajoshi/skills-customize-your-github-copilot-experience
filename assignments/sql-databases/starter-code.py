import sqlite3
from datetime import datetime

# Database setup
DATABASE_FILE = "school_system.db"

def create_connection():
    """Connect to the SQLite database."""
    connection = sqlite3.connect(DATABASE_FILE)
    return connection

def create_schema():
    """Create the database schema with tables."""
    conn = create_connection()
    cursor = conn.cursor()
    
    # TODO: Create the students table
    # Columns: student_id (INTEGER PRIMARY KEY), name (TEXT), email (TEXT), 
    #          grade_level (INTEGER), enrollment_date (TEXT)
    
    
    # TODO: Create the courses table
    # Columns: course_id (INTEGER PRIMARY KEY), course_name (TEXT), 
    #          instructor (TEXT), credits (INTEGER), description (TEXT)
    
    
    # TODO: Create the enrollments table
    # Columns: enrollment_id (INTEGER PRIMARY KEY), student_id (INTEGER FOREIGN KEY),
    #          course_id (INTEGER FOREIGN KEY), enrollment_date (TEXT), grade (TEXT)
    
    
    conn.commit()
    conn.close()

def add_student(name, email, grade_level):
    """Add a new student to the database."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        enrollment_date = datetime.now().strftime("%Y-%m-%d")
        # TODO: Insert a new student
        conn.commit()
        print(f"Student {name} added successfully!")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()

def get_all_students():
    """Retrieve and display all students."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # TODO: Query all students from the students table
        # TODO: Display results in a readable format
        pass
    except sqlite3.Error as e:
        print(f"Error retrieving students: {e}")
    finally:
        conn.close()

def update_student_grade(student_id, course_id, grade):
    """Update a student's grade in a specific course."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # TODO: Update the grade in the enrollments table
        conn.commit()
        print(f"Grade updated for student {student_id} in course {course_id}")
    except sqlite3.Error as e:
        print(f"Error updating grade: {e}")
    finally:
        conn.close()

def delete_enrollment(enrollment_id):
    """Delete an enrollment record."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # TODO: Delete the enrollment record
        conn.commit()
        print(f"Enrollment {enrollment_id} deleted successfully!")
    except sqlite3.Error as e:
        print(f"Error deleting enrollment: {e}")
    finally:
        conn.close()

def get_student_courses(student_id):
    """Get all courses a student is enrolled in."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # TODO: Use JOIN to get courses and grades for a specific student
        pass
    except sqlite3.Error as e:
        print(f"Error retrieving courses: {e}")
    finally:
        conn.close()

def get_average_grade_per_course():
    """Calculate average grade per course."""
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        # TODO: Use GROUP BY and AVG() to calculate average grades
        pass
    except sqlite3.Error as e:
        print(f"Error retrieving averages: {e}")
    finally:
        conn.close()

# Main execution
if __name__ == "__main__":
    # TODO: Call create_schema() to set up the database
    # TODO: Add sample data
    # TODO: Test all functions
    pass
