# -*- coding: utf-8 -*-
from flask import *
from flask import Blueprint, render_template, request, redirect, Response, session, url_for, jsonify
from datetime import timedelta
import  plat
import comanda





app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)


@app.route("/",methods=["GET","POST"])
def index():
    entrants = plat.get_plat_by_tipus('Entrant')
    primers = plat.get_plat_by_tipus('Primer')
    segons =  plat.get_plat_by_tipus('Segon')
    postres =  plat.get_plat_by_tipus('Postres')
    
    if(request.method == "POST"):
        #Actualitzem numComanda i taula
        numComanda = comanda.get_last_comanda_num()[0] + 1
        taula = comanda.get_available_taula()[0] + 1 
        for name, quantitat in request.form.items():
            comanda.insert_comanda(numComanda, name, int(quantitat), taula)
        msg = "Comanda afegida correctament!"
        return render_template('/carta.html', entrants = entrants, primers = primers,segons=segons, postres=postres, msg=msg)
    
    if(request.method == "GET"):
        print("get")
        return render_template('/carta.html', entrants = entrants, primers = primers,segons=segons, postres=postres)
    
    

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
@GET /comandes
    return totes les comandes
@POST /comandes
    elimina comanda
"""

@app.route("/comandes", methods=["GET", "POST"])
def comandes():
    if(request.method =="GET"):
        comandes = comanda.get_comanda_all()
        return render_template('/comandes.html',comandes=comandes)

    if(request.method =="POST"):
        id = request.form.get('id')
        if(comanda.get_comanda_by_num(id)):
            comanda.delete_commanda(id)
            msg="Comanda "+ str(id) + " eliminada correctament"
            comanda_info = comanda.get_comanda_all()
            return render_template('/comandes.html',comandes=comanda_info, msg=msg, valid=True) 
        msg= "Ops! No hi ha comanda amb l'identificador "+ str(id)
        comanda_info = comanda.get_comanda_all()
        return render_template('/comandes.html',comandes = comanda_info, msg=msg, valid=False) 
    return render_template('/comandes.html',comandes=[])
    



"""
@GET comanda/:numComanda
    retorna aquesta comanda

@DELETE /comanda/:numComanda 
    elimina comanda
"""
@app.route("/comanda/<id>", methods=["GET", "POST"])
def get_comanda(id):
    if(request.method =="GET"):
        comanda_info = comanda.get_comanda_by_num(id)
        return render_template('/comandes.html',comandes=comanda_info, oneComanda=True) 
    if(request.method =="POST"):
        id = request.form.get('id')
        plat_info = request.form.get('plat')
        print(id,plat_info)

        if(comanda.get_comanda_by_num_plat(id,plat_info)):
            comanda.delete_commanda_plat(id, plat_info)
            msg="Comanda "+ id +" plat " + str(plat_info) + " eliminada correctament"
            comanda_info = comanda.get_comanda_by_num(id)
            return render_template('/comandes.html',comandes=comanda_info, msg=msg, valid=True) 
        msg= "Ops! No hi ha comanda amb l'identificador "+ id+ " i el plat "+ str(plat_info)
        comanda_info = comanda.get_comanda_by_num(id)
        return render_template('/comandes.html',comandes = comanda_info, msg=msg, valid=False) 
    return render_template('/comandes.html',comandes=[])


@app.errorhandler(404)
def page_not_found(e):
    return render_template("/error_404.html")

