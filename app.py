from flask import Flask, request 

app = Flask(__name__)

@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "You made a GET request"
    elif request.method == "POST":
        return "You made a POST request"
    else: 
        return "You will never see this message"

@app.route("/handle_url_params")
def handle_params():
    greeting  = request.args["greeting"]
    name = request.args.get("name")
    return f"{greeting} {name}"

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5555, debug=True)