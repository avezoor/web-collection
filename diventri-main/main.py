from app import app  # noqa: F401
from config import HOST, PORT, DEBUG

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
