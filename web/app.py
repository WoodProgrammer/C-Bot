from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/set_payload")
def set_payload():
    print(request)

    ##setting_payload
    return render_template("payloads.html")


@app.route("/payload/<id>")
def payload_detail(id):
    return render_template("payloads.html")


if __name__ == "__main__":
    app.run(debug=True)
