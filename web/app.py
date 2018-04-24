from flask import Flask, render_template, request
from models import Model
import os


app = Flask(__name__)
obj = Model()
app.config['UPLOAD_FOLDER'] = "scripts"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/set_payload",methods=["GET","POST"])
def set_payload():
    payload_dict = {}

    if request.method == "POST":
        file_name = request.form['payload_name']
        file = request.files['file_of_code']
        vars = [var for var in request.form['payload_variables'].split(',')]

        payload_dict['payload_name'] = file_name

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name+".py")) #file is saving in here
        payload_dict['vars'] = vars
        payload_dict['file'] = 'scripts/{}'.format(file_name)#file path

        obj._set_payload(payload_dict) ## saving to the db

        return render_template("payloads.html",data="Payload {} Kayıt edildi".format(file_name))


@app.route("/payload/<id>")
def payload_detail(id):
    return render_template("payloads.html")


if __name__ == "__main__":
    app.run(debug=True)
