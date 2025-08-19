from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Anaylst',
        'location': 'Bengaluru, India',
        'salary' : 'Rs. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Dehli, India',
        'salary' : 'Rs. 15,00,000'
    },
        {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        # 'salary' : 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'location': 'San Francisco, USA',
        'salary' : '$ 120,000'
    }
]

@app.route("/") # main route to home page ; empty path
def hello_jovian():
    return render_template("index.html", jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


