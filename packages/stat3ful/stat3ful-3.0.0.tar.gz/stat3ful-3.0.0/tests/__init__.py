import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path = [BASE_DIR, *sys.path]
