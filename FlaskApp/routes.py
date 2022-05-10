# -*- coding: utf-8 -*-
from flask import *
from flask import Blueprint, render_template, request, redirect, Response, session, url_for
from datetime import timedelta
import datetime
""" import  plat
import comanda """
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
    return render_template('/index.html')

@app.route("/index")
def index_bar():
    return redirect(url_for('index'))





# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("/error_404.html")
