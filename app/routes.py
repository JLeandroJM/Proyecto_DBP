from app import app
from flask import render_template, request
from app import db
from app.models import User
import requests
import json

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add/user", methods=['GET'])
def addUser():
    try:
        args = request.args
        username = args.get("username")
        password = args.get("password")
        email = args.get("email")

        if (username == None):
            return "Falta parametro username"
        elif (password == None):
            return "Falta parametro password"
        elif (email == None):
            return "Falta parametro email"
        
        if (not verifyPassword(password)):
            return "Contrasena invalida"
        #returnString = "Username: " + username + " Password: " + password + "Email: " + email
        newUser = User(username=username, password=password, email=email)
        db.session.add(newUser)
        db.session.commit()
    except Exception as error:
        print("Invalid user", error)
        return "Invalid user"       
    return "User added"

def verifyPassword(password):
    return len(password) >= 10

def miFuncion():
    return "hola"