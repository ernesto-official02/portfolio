from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -----------------------
# Routes
# -----------------------

@app.route("/")
def home():
    """Home page"""
    return render_template("index.html")


# -----------------------
# App Runner
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
