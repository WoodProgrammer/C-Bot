from flask import Flask, render_template, request
from models import Model
from helper import hash_file_name
import os

app = Flask(__name__)
obj = Model()
app.config['UPLOAD_FOLDER'] = "scripts"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/set_payload",methods=["GET","POST"])
def set_payload():
    if request.method == "POST":
        file_name = request.form['payload_name']
        file = request.files['file_of_code']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], hash_file_name(file_name)))

        return render_template("payloads.html")


@app.route("/payload/<id>")
def payload_detail(id):
    return render_template("payloads.html")


if __name__ == "__main__":
    app.run(debug=True)
