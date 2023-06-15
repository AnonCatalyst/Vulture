from flask import Flask, render_template, request
import requests
import urllib.parse
import threading
import random
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/search", methods=["POST"])
def search():
    username = request.form["username"]
    results = []
    with open("urls.txt", "r") as f:
        for line in f:
            url = urllib.parse.urljoin(line, username)
            try:
                s = requests.Session()
                s.headers.update({"User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(98, 100)}.0.{random.randint(4840, 4849)}.{random.randint(80, 89)} Safari/537.36"})
                response = s.get(url)
                status_code = response.status_code
                if status_code == 200:
                    results.append({"url": url, "status_code": status_code})
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.TooManyRedirects:
                pass
    return render_template("index.html", results=results)
if __name__ == "__main__":
    app.run(debug=True)
