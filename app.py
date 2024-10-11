from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/api/words", methods=["GET"])
def scrape():
    url = "https://justinjackson.ca/words.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = {
        "page_title": soup.title.string if soup.title else "No title found",
        "titles": [
            h.get_text() for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        ],
        "paragraphs": [p.get_text() for p in soup.find_all("p")],
        "lists": [li.get_text() for li in soup.find_all("li")],
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
