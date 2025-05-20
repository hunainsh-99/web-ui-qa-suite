from flask import Flask, request, send_from_directory
import os

# Serve out of the repo root, with pages/ as a subfolder
app = Flask(__name__, static_folder=os.getcwd())

# GET any file under pages/
@app.route('/pages/<path:filename>', methods=['GET'])
def serve_page(filename):
    return send_from_directory('pages', filename)

# POST to /pages/login.html: replicate the JS logic
@app.route('/pages/login.html', methods=['POST'])
def handle_login():
    u = request.form.get('user', '')
    p = request.form.get('pass', '')
    if not u or not p:
        return 'both fields required'
    if u != 'admin' or p != 'secret':
        return 'invalid credentials'
    return 'welcome, admin'

if __name__ == '__main__':
    # listen on all interfaces so CI can hit it
    app.run(host='0.0.0.0', port=8000)
