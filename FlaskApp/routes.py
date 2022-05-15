# -*- coding: utf-8 -*-
from flask import *
from flask import Blueprint, render_template, request, redirect, Response, session, url_for, jsonify
from datetime import timedelta
import datetime
import  plat
import comanda
import functools
import random




app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)

# def login_required(func):
#     @functools.wraps(func)
#     def secure_function():
#         if not session:
#             return redirect(url_for("login", next=request.url))
#         return func()
#     return secure_function

# def admin_required(func):
#     @functools.wraps(func)
#     def secure_function_admin():
#         if session:
#             if (session["rol"]) != "Administrador":
#                 return redirect(url_for("index"))
#             return func()
#         else:
#             return(redirect(url_for("login",next=request.url)))
#     return secure_function_admin

# def not_logged(func):
#     @functools.wraps(func)
#     def secure_function_logged():
#         #TODO: Mirar de loggegar des de diferents dispositius
#         if(session["rol"] == "Administrador"):
#             return redirect(url_for("admin"))
#         elif(session["rol"] == "Client"):
#             return redirect(url_for("client"))
#         return func()
#     return secure_function_logged

@app.route("/")
def index():
    return render_template('/carta.html')

@app.route("/login")
def login():
    return render_template('/login.html')





#############
# API REST
#############


"""
@GET carta
    retorna tots els plats
"""
@app.route("/carta",methods = ["GET"])
def carta():
    if(request.method == "GET"):
        content = plat.get_carta()
    return jsonify(content)

"""
@GET /comanda(actualDay = false)
    return totes les comandes des de sempre
"""



"""
@GET /comanda(actualDay = true)
    return totes les comandes d'avui
@POST /comanda
    insert comanda
"""

@app.route("/comandes")
def comandes():
    comandes = comanda.get_comanda_all()
    return render_template('/comandes.html',comandes=comandes)



""" @app.route("/comanda",methods = ["GET","POST"])
def comanda(actualDay):
    if(request.method == "GET"):
    if(request.method == "POST"):
    return """

"""
@GET comanda/:numComanda
    retorna aquesta comanda
@POST comanda/:numComanda
    modifica aquesta comanda
@DELETE /comanda/:numComanda 
    elimina comanda
"""
""" @app.route("/comanda/<numComanda>",methods = ["GET","POST","DELETE"])
def changeComanda():
    if(request.method == "GET"):
    if(request.method == "DELETE"):

    return render_template('/index.html')
 """


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("/error_404.html")



"""
TODO: 
-Afegir data i hora comanda

@GET carta
    retorna tots els plats

@GET /comanda(actualDay = false)
    return totes les comandes des de sempre
@GET /comanda(actualDay = true)
    return totes les comandes d'avui
@POST /comanda
    insert comanda

@GET comanda/:numComanda
    retorna aquesta comanda
@POST comanda/:numComanda
    modifica aquesta comanda
@DELETE /comanda/:numComanda 
    elimina comanda
"""