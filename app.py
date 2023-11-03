from flask import Flask, render_template, request, jsonify
import evanbot
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.get("/")
def base_page():
    return render_template("home.html")

@app.route("/evan_bot", methods=["POST"])
def qna():
    # print('Im hit')
    # question = request.json["message"]
    question = request.get_json().get("message")
    response = evanbot.evanbot(question)
    msg = {"answer": response}

    return jsonify(msg)



if __name__ == "__main__":
    app.run(debug=True)