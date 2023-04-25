from flask import Flask, jsonify, render_template
from flask import Flask, jsonify
from quote import breaking_quote

application = Flask(__name__)


@application.route("/")
def index():
    return render_template('index.html')


@application.route("/quote")
def quote():
    random_quote = breaking_quote()
    return jsonify({"quote": random_quote})


if __name__ == "__main__":
    application.run(debug=True).run(debug=True)
