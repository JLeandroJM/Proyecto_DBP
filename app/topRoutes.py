from app import app
from flask import render_template, request
from app import db
from app.models import User
import requests
import json

#ruta base
@app.route("/")
def index():
    return render_template("index.html")