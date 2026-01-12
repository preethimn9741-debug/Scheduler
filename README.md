# Python Job Scheduler Application

This project is a **Python-based Job Scheduler** that executes background jobs at defined intervals.  
It has been extended into a **robust full-stack application** using a web interface, database-backed CRUD operations, and automated testing.

## Features

- Background job scheduling using Python
- Executes independent job scripts at fixed intervals
- Flask-based web application to view and manage jobs
- CRUD backend with SQLite database
- Interactive frontend using HTML and JavaScript
- Persistent job storage
- Logging for job execution and failures
- Automated test support using pytest

## Technologies Used

- **Python**
- **Flask** – Web framework
- **SQLite** – Database
- **Subprocess** – Job execution
- **Logging** – Scheduler logs
- **HTML / JavaScript** – Frontend UI
- **Pytest** – Testing

  ## 📂 Project Structure

scheduler/

│── scheduler.py # Scheduler engine

│── app.py # Flask web application

│── database.py # Database and CRUD operations

│── jobs.json # Initial job configuration

│── jobs.db # SQLite database

│── job1.py # Sample job

│── scheduler.log # Execution logs

├── templates/

│ └── index.html # Web UI

├── static/

│ └── script.js # JavaScript for UI interaction

├── tests/

│ └── test_scheduler.py # Test cases

## Installation & Setup

1. Navigate to the project directory

   cd C:\scheduler

2. Create and activate virtual environment

   python -m venv venv
   
   venv\Scripts\activate

3. Install dependencies

   pip install flask pytest

4. Start the Flask Web App

   python app.py

5. Running Test Cases

   python -m pytest
   
## output 

Scheduler started... Press CTRL+C to stop

## terminal screnshort output 

<img width="800" height="533" alt="image" src="https://github.com/user-attachments/assets/35f83122-d85c-4a29-a0da-9d5471413a82" />

## Conclusion

This project demonstrates a complete Python-based job scheduling system with real-time execution and monitoring. By integrating a Flask web interface, database-backed job management, and automated testing, the application reflects real-world backend development practices. The use of a VS Code–based workflow, logging, and error handling ensures reliability and maintainability. Overall, the project showcases practical skills in Python, web development, and system automation.





  
