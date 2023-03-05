from flask import Flask
from web_scraping_classcentral import get_data

app = Flask(__name__)


@app.get("/class_central")
def class_central():
    data = get_data()
    return data


if __name__ == "__main__":
    app.run(debug=True, port = 8000)
