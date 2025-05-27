from flask import Flask, send_from_directory, request
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PAGES_DIR    = os.path.join(PROJECT_ROOT, "pages")

app = Flask(__name__, static_folder=None)

@app.route("/pages/login.html", methods=["POST"])
def login():
    u = request.form.get("user", "")
    p = request.form.get("pass", "")
    if not u or not p:
        msg = "both fields required"
    elif u != "admin" or p != "secret":
        msg = "invalid credentials"
    else:
        msg = f"welcome, {u}"
    return msg, 200

@app.route("/pages/<path:filename>", methods=["GET"])
def serve_page(filename):
    return send_from_directory(PAGES_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
