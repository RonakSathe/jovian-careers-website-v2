from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import *
app = Flask(__name__)

        


@app.route('/')
def hello_world():
  jobs  = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name="Hi-MENIN")


@app.route('/api/jobs')
def list_jobs():
  jobs  = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job[0])



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
