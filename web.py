import urllib.parse
import threading
import random
import requests
from flask import Flask, render_template, request
try:
    app = Flask(__name__)
    @app.route("/")
    def index():
        return render_template("index.html")
    @app.route("/search", methods=["POST"])
    def search():
        user_name = request.form["username"]
        results = []
        with open("urls.txt", "r") as f:
            for line in f:
                url = urllib.parse.urljoin(line, user_name)
                try:
                    s = requests.Session()
                    s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4758.102 Safari/537.36"})
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
except KeyboardInterrupt:
    os.system("clear")
    bannerx = print("""
 Project: Vulture
 Category: Username Search
 Developer: AnonCatalyst
   [1] ~ Terminal
   [2] ~ Web Ui
   ---------------------
     00: Exit""")
