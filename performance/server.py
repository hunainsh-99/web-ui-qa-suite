from flask import Flask, send_from_directory
import os

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), '../pages'),
    static_url_path='/pages'
)


@app.route('/pages/<path:filename>')
def serve_page(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
