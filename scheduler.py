import time
import json
import subprocess
import logging
import os


logging.basicConfig(
    filename="scheduler.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with open("jobs.json", "r") as f:
    jobs = json.load(f)

# Add last_run time to each job
for job in jobs:
    job["last_run"] = 0

print("Scheduler started... Press CTRL+C to stop")

try:
    while True:
        current_time = time.time()

        for job in jobs:
            if current_time - job["last_run"] >= job["interval"]:
                logging.info(f"Running job: {job['name']}")

                try:
                    result = subprocess.run(
                        ["python", job["script"]],
                        capture_output=True,
                        text=True
                    )

                    if result.returncode == 0:
                        logging.info(f"{job['name']} completed successfully")
                    else:
                        logging.error(f"{job['name']} failed: {result.stderr}")

                except Exception as e:
                    logging.error(f"{job['name']} error: {str(e)}")

                job["last_run"] = current_time

        time.sleep(1)

except KeyboardInterrupt:
    print("\nScheduler stopped gracefully")
    logging.info("Scheduler stopped by user")

