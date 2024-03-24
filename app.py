
from flask import Flask, render_template

app = Flask(__name__,template_folder="templates")

JOBS = [
  {
    'id': 1,
    'title': "Frontend Engineer",
    'location': "Remote",
    'salary': "Rs 10,000"
  },
  {
    'id': 2,
    'title': "Backend Engineer",
    'location': "Remote",
    'salary': "Rs 1,00,000"
  },
  {
    'id': 3,
    'title': "Data Analyst",
    'location': "Remote",
  },
  {
    'id': 4,
    'title': "Data Scientist",
    'location': "Remote",
    'salary': "Rs 15,000"
  }
]


@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,company_name="Jovian")
 # return "Hello World!"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
