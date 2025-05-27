from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder=None)

@app.route('/pages/<path:filename>', methods=['GET'])
def serve_page(filename):
    return send_from_directory('pages', filename)

@app.route('/pages/login.html', methods=['POST'])
def login():
    u = request.form.get('user', '')
    p = request.form.get('pass', '')
    if not u or not p:
        msg = 'both fields required'
    elif u != 'admin' or p != 'secret':
        msg = 'invalid credentials'
    else:
        msg = 'welcome, admin'
    return msg, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
