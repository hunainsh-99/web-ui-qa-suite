import os
import sys
import subprocess
import time
import socket
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1) ensure repo root on PYTHONPATH so "import pages.*" works
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

@pytest.fixture(scope="session", autouse=True)
def flask_server():
    """
    Launch performance/server.py on :8000 for static pages.
    """
    cmd = ["python", os.path.join(ROOT, "performance", "server.py")]
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # wait for it to bind
    for _ in range(20):
        try:
            sock = socket.create_connection(("127.0.0.1", 8000), timeout=1)
            sock.close()
            break
        except OSError:
            time.sleep(0.5)
    else:
        proc.kill()
        pytest.exit("❌ could not start Flask server on port 8000")

    yield

    proc.terminate()
    proc.wait()

@pytest.fixture(scope="session", name="base")
def base_url():
    """
    Base URL for UI tests. 
    Override by setting BASE_URL, otherwise use our flask_server.
    """
    return os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # pick up custom Chrome binary if CI set it
    chrome_bin = os.getenv("CHROME_BIN")
    if chrome_bin:
        options.binary_location = chrome_bin

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

