import sys, os

BASE_DIR = os.path.join(os.path.dirname(__file__))

sys.path.insert(0, BASE_DIR)

from src import app as application