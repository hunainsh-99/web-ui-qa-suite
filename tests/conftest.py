import os
import pytest

@pytest.fixture(scope="session")
def base():
    # In CI we’ll set BASE_URL, locally we fall back to file://<project_root>
    if os.getenv("BASE_URL"):
        return os.getenv("BASE_URL")
    local = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return f"file://{local}"
