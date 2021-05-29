from flask import Flask 
from flask import render_template

app = Flask(__name__, template_folder="static")

@app.route("/")
def hello():
    message = ""
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)




