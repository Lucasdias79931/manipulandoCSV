from consultas import Dataset as DB
from flask import Flask, render_template
import sys
import os
import pandas as pd



here = os.path.abspath(os.path.dirname(__file__))

datasestsPath = os.path.join(here, "upload")

os.makedirs(datasestsPath, exist_ok= True)

db = DB(datasestsPath)

app = Flask(__name__)




if __name__ == "__main__":
    
    
    app.run(debug=True)