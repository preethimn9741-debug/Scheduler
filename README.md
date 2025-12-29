
# Job Scheduler

## Project Description
This project is a **simple job scheduler** written in Python.
It reads job details from a JSON file and executes the specified Python scripts at fixed time intervals.
All job execution details are logged to a log file.

---

## Files
- `scheduler.py` – Main scheduler script
- `jobs.json` – Job configuration file
- `job1.py` – Example job script
- `scheduler.log` – Log file generated during execution
- `README.md` – Project documentation

---

## How the Scheduler Works
1. Loads job definitions from `jobs.json`
2. Each job contains:
   - Job name
   - Python script to execute
   - Time interval (in seconds)
3. The scheduler continuously checks if a job is ready to run
4. When the interval is reached:
   - The job script is executed
   - Success or failure is logged
5. The scheduler runs until stopped manually

---

## Job Configuration
Jobs are defined in `jobs.json`.

Each job includes:
- `name` – Job name
- `script` – Python script to execute
- `interval` – Execution interval in seconds

---

## How to Run

python scheduler.py

## Output

Job execution status is printed to the console

Detailed logs are written to:

scheduler.log




