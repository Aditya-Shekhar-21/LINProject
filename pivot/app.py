from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = [{"Date":"09-09-21",
    "Req ID" : "1",
    "Username" : "Admin",
    "Status" : "Running"
    },
    ]
    return render_template('index.html',data=data)

@app.route('/output/')
def output():
    return "<h>Your Record successfully stored!</h>"

if __name__ == '__main__':
    app.run()