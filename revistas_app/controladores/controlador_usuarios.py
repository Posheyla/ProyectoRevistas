from flask import render_template, request, redirect, session,flash
from revistas_app import app 
from revistas_app.modelos.modelo_usuarios import Usuario
from flask_bcrypt import Bcrypt
import re

EXP_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)

@app.route( '/', methods=['GET'] )
def paginaInicio():
    return render_template( "inicio.html" )

@app.route('/registro', methods=['POST'])
def registrarUsuario():
    if request.form["nombre"] == '' or request.form["apellido"] == '' or request.form["email"] == '' or request.form["password"] == '' or request.form["confpassword"] == '':
        flash("Ingrese los datos en blanco","registrar")
        return redirect('/')
    else:
        if len(request.form["nombre"])>3:
            if len(request.form["apellido"])>3:
                if EXP_EMAIL.match(request.form["email"]):
                    if int(len(request.form["password"])>= 8):
                        if request.form["password"] == request.form["confpassword"]:
                            passwordEncriptado= bcrypt.generate_password_hash(request.form["password"])
                            nuevoUsuario = {
                                "nombre" : request.form["nombre"],
                                "apellido" : request.form["apellido"],
                                "email" : request.form["email"],
                                "password" : passwordEncriptado,
                                "conf_password" : request.form["confpassword"]
                            }
                            session["nombre"] = request.form["nombre"]
                            session["email"] = request.form["email"]
                            resultado = Usuario.agregarUsuario(nuevoUsuario)
                            return redirect('/dashboard')
                        else:
                            flash("Password no coincide","registrar")
                            return redirect('/')
                    else:
                        flash("Error,password muy pequeño","registrar")
                        return redirect('/')
                else:
                    flash("Error,no cumple el formato de correo","registrar")
                    return redirect('/')
            else:
                flash("Error,apellido menor a 3 letras,ingrese de nuevo otro apellido","registrar")
                return redirect('/')
        else:
            flash("Error,nombre menor a 3 letras,ingrese de nuevo otro nombre","registrar")
            return redirect('/')


@app.route('/login', methods=['POST'])
def iniciarSesion():

    loginEmail = request.form["loginEmail"]
    loginPassword = request.form["loginPassword"]
    
    usuario ={
        "email" : loginEmail,
        "password" : loginPassword
    }
    resultado = Usuario.verificarUsuario(usuario)

    if resultado == None:
        flash("No se encuentra registrado","login")
        return redirect('/')
    else:
        if not bcrypt.check_password_hash(resultado.password, loginPassword):
            flash("El password es incorrecto","login")
            return redirect('/')
        else: 
            session["nombre"] = resultado.nombre
            session["email"] = resultado.email

            return redirect( '/dashboard')


@app.route('/addmagazine', methods=['GET'])
def agregarMagazine():
    return render_template('new.html')


@app.route( '/logout', methods=["GET"] )
def cerrarUsuario():
    session.clear()
    return redirect( '/' )

@app.route('/update/<autor>',methods=["POST"])
def editarUsuario(autor):
    usuarioAEditar ={
        "email" : request.form["email"],
        "nombre" : autor,
        "apellido" : request.form["apellido"],
    }
    print(usuarioAEditar)
    resultado = Usuario.editarUsuario(usuarioAEditar)
    session["nombre"] = request.form["nombre"]
    session["email"] = request.form["email"]
    return redirect('/dashboard')
