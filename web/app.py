from flask import Flask, render_template, request
from models import Model
app = Flask(__name__)
obj = Model()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/set_payload")
def set_payload():

    payload_name = request.args['payload_name']
    payload_function = request.args['payload_function']
    payload_variables = request.args['payload_variables']
    service_selection = request.args['service_selection']
    

    return render_template("payloads.html")


@app.route("/payload/<id>")
def payload_detail(id):
    return render_template("payloads.html")


if __name__ == "__main__":
    app.run(debug=True)
