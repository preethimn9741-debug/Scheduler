from flask import Flask, request, jsonify, render_template
from database import init_db, add_job, get_jobs

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/jobs", methods=["GET"])
def jobs():
    return jsonify(get_jobs())

@app.route("/jobs", methods=["POST"])
def create_job():
    data = request.json
    add_job(data["name"], data["script"], data["interval"])
    return {"message": "Job added"}, 201

if __name__ == "__main__":
    app.run(debug=True)
