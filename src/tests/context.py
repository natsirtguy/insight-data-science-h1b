'''Allow tests to import from src.'''
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))

import src.h1b_counting as h1b_counting
