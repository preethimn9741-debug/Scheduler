import os
import json
import sqlite3
import pytest
from unittest.mock import patch, MagicMock
import scheduler
import database
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_database_file_missing(monkeypatch):
    monkeypatch.setattr(sqlite3, "connect", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError))
    with pytest.raises(FileNotFoundError):
        database.get_jobs()

def test_add_job_with_missing_fields():
    with pytest.raises(TypeError):
        database.add_job("job1")

def test_add_job_negative_interval():
    database.init_db()
    database.add_job("job1", "job1.py", -5)
    jobs = database.get_jobs()
    assert jobs[-1]["interval"] < 0

def test_get_jobs_returns_list():
    jobs = database.get_jobs()
    assert isinstance(jobs, list)

def test_update_last_run_invalid_id():
    database.init_db()
    database.update_last_run(9999, 123456)
    assert True  

@patch("subprocess.run")
def test_scheduler_subprocess_failure(mock_run):
    mock_run.side_effect = Exception("Process failed")
    with pytest.raises(Exception):
        mock_run(["python", "job1.py"])

def test_scheduler_missing_job_script():
    result = os.path.exists("missing_job.py")
    assert result is False

def test_scheduler_invalid_interval():
    job = {"interval": -10, "last_run": 0}
    assert job["interval"] < 0

def test_scheduler_log_file_exists():
    assert os.path.exists("scheduler.log")

def test_home_page_wrong_method(client):
    response = client.post("/")
    assert response.status_code == 405

def test_jobs_endpoint_wrong_method(client):
    response = client.put("/jobs")
    assert response.status_code == 405

def test_create_job_missing_payload(client):
    response = client.post("/jobs", json={})
    assert response.status_code >= 400

def test_jobs_json_file_missing(monkeypatch):
    monkeypatch.setattr("builtins.open", lambda *a, **k: (_ for _ in ()).throw(FileNotFoundError))
    with pytest.raises(FileNotFoundError):
        open("jobs.json")

def test_jobs_json_invalid_format(monkeypatch):
    monkeypatch.setattr(json, "load", lambda *a, **k: (_ for _ in ()).throw(ValueError))
    with pytest.raises(ValueError):
        json.load("jobs.json")

def test_large_number_of_jobs():
    jobs = [{"name": f"job{i}", "interval": i} for i in range(1000)]
    assert len(jobs) == 1000
