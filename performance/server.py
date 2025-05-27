import os
from flask import Flask, send_from_directory


def create_app():
    # Determine the pages directory relative to this file
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    pages_dir = os.path.join(base_dir, "pages")

    # Create Flask app, serving static files from pages_dir at /pages
    app = Flask(
        __name__,
        static_folder=pages_dir,
        static_url_path="/pages"
    )

    @app.route("/pages/<path:filename>")
    def serve_page(filename):
        # send file from pages directory
        return send_from_directory(pages_dir, filename)

    return app


if __name__ == "__main__":
    # Run the app on host 0.0.0.0 so Locust/GitHub Actions can reach it
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
