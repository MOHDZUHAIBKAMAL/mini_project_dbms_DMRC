# Backend Social Media App

A distributed backend application for social media functionality with multiple microservices.

## Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- Visual Studio Code
- Postman (optional)

## Installation Guide

### Step 1: Download Repository
- Go to `https://github.com/MOHDZUHAIBKAMAL/Social_media_app_with_explore_function.git`
- Click on "Code" button
- Select "Download ZIP"

### Step 2: Extract and Open Project
**Windows:**
```bash
# Extract the ZIP file
Right-click > Extract All

# Open in VS Code
cd social-media-backend
code .
```

**Mac:**
```bash
# Extract the ZIP file
unzip social-media-backend.zip

# Open in VS Code
cd social-media-backend
code .
```

### Step 3: Create Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

**Mac:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### Step 4: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 5: Configure Python Path

1. Locate your Python path in virtual environment:

**Windows:**
```bash
where python
# Copy the path that shows under venv folder
```

**Mac:**
```bash
which python
# Copy the path that shows under venv folder
```

2. Open `app_runner.py` and replace the existing Python path with your copied path:
```python
# Example path - replace with your actual path
PYTHON_PATH = '<highlight>your_venv_python_path_here</highlight>'
```

### Step 6: Database Configuration

1. In each app's `app.py` file, update the MySQL configuration:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<highlight>your_mysql_password</highlight>@localhost/<highlight>your_database_name</highlight>'
```

2. Create database in MySQL:

**Windows/Mac MySQL Command Line:**
```sql
mysql -u root -p
CREATE DATABASE social_media_app_zubi;
-- If database exists:
DROP DATABASE social_media_app_zubi;
CREATE DATABASE social_media_app_zubi;
```

### Step 7: Initialize Database

```bash
# Navigate to shared folder
cd shared

# Initialize database
flask db init

# Create and apply migrations
flask db migrate
flask db upgrade

# Return to root directory
cd ..
```

### Step 8: Run the Application
```bash
python app_runner.py
```

The server will start and display available endpoints in the terminal.

[Previous sections remain the same until Testing the Application]

## Testing the Application

### Option 1: Using Postman
1. Open Postman
2. Import the provided Postman collection file (`zuhaib flask sample inputs.postman_collection`)
   - The collection includes pre-configured routes, methods, and sample input data
   - Each request contains example payloads and required headers
3. Test the endpoints shown in terminal

Example endpoints:
- User Service: `http://localhost:5001/api/users`
- Post Service: `http://localhost:5002/api/posts`

### Option 2: Using SQL Files and Browser
If you prefer using SQL directly:

1. **Important**: Choose ONE of these approaches:
   
   **Approach A - Flask Migration:**
   - Follow Step 7 (Initialize Database) as described above
   - Proceed with testing endpoints
   
   **Approach B - Direct SQL:**
   - Skip Step 7 (Initialize Database)
   - Execute the provided SQL files in MySQL:
   ```sql
   source sample input for sql
   ```

2. Test the endpoints in your preferred browser using the routes displayed in terminal
   - The SQL file provides pre-populated data for testing
   - No additional data insertion required

**Note**: Do not mix both approaches as it may cause table conflicts.
