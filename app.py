from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Colombo, Sri Lanka',
    'salary': "LKR 1,500,000"
  },
  {
    'id': 2,
    'title': 'Machine Learning Engineer',
    'location': 'London, UK',
    #'salary': "GBP 2,500"
  },
  {
    'id': 3,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': "INR 1,000,000"
  },
  {
    'id': 4,
    'title': 'Cloud Architect',
    'location': 'Remote',
    'salary': "LKR 2,000,000"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
