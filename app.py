from flask import Flask, request, jsonify
import pyshorteners

app = Flask(__name__)

def shorten_url(url):
    shortener = pyshorteners.Shortener()
    return shortener.tinyurl.short(url)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/shorten", methods=["POST"])
def shorten_url_endpoint():
    long_url = request.json["url"]
    short_url = shorten_url(long_url)
    return jsonify({"shortUrl": short_url})

if __name__ == "__main__":
    app.run(debug=True)
