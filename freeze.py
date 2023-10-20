from flask_frozen import Freezer
from main import app  # Importing the Flask app instance from your main.py

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()

