from flask import Flask, render_template, request, redirect, session
from revistas_app import app 
from revistas_app.modelos.modelo_revistas import Revista

@app.route('/dashboard', methods=['GET'])
def abrirDashboard():
    nombre = session["nombre"]
    resultado = Revista.obtenerListaDeMagazinesConUsuarios()
    return render_template("dashboard.html",resultado= resultado,nombre=nombre)

@app.route('/addmagazine',methods=['POST'])
def agregarDatosMagazine():

    nuevaRevista = {
        "autor" : session["nombre"],
        "titulo" : request.form["title"],
        "contenido" : request.form["description"],
        "usuario_email" : session["email"]
        }

    print(nuevaRevista)
    resultado = Revista.agregarRevista(nuevaRevista)
    return redirect('/dashboard')

@app.route('/show/<id>', methods=['GET'])
def mostrarContenidoRevista(id):
    revistaAMostrar={ 
        "id" : id
    }
    revista =Revista.obtenerRevista(revistaAMostrar)
    
    return render_template( "show.html", revista=revista[0] )

@app.route('/<user>/account',methods=['GET'])
def mostrarRevistas(user):
    revistasAMostrar={ 
        "autor" : user
    }
    usuario =Revista.desplegarRevistas(revistasAMostrar)
    print(usuario)
    return render_template( "account.html", usuario=usuario,user=user)

@app.route('/delete/<id>',methods=["POST"])
def eliminarUnaRevista(id):
    RevistaAEliminar={ 
        "id" : id
    }
    resultado = Revista.eliminarRevista(RevistaAEliminar)
    return redirect('/dashboard')
