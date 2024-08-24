from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def company():
    return render_template("home.html")

@app.route("/person/")
def person():
    context = {
        "link": "Сайт компании"
    }
    return render_template("about.html", **context)


if __name__ == "__main__":
    app.run()