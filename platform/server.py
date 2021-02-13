from flask import Flask
import searcher
from flask import request
import websiteparser

app = Flask(__name__)
@app.route("/get-results", methods=["GET", "POST"])
def index():
    query = request.args.get("claim")
    websiteDict = searcher.searchGoogle(query)
    articleDict = websiteparser.parse(websiteDict)
    return articleDict

if __name__ == "__main__":
    app.run(debug=True)

