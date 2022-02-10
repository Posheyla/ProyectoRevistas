from revistas_app.config.mysqlconnection import MySQLConnection,connectToMySQL

class Usuario:
    def __init__(self,nombre,apellido,email,password,conf_password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.conf_password = conf_password

    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "INSERT INTO usuarios(nombre,apellido,email,password,conf_password) VALUES(%(nombre)s,%(apellido)s,%(email)s,%(password)s,%(conf_password)s)"
        resultado = connectToMySQL("schema_magazines").query_db(query,nuevoUsuario)
        return resultado

    @classmethod
    def verificarUsuario(cls,usuario):
        query = "SELECT * FROM usuarios WHERE email= %(email)s;"
        resultado = connectToMySQL("schema_magazines").query_db(query,usuario)
        if len(resultado)>0:
            usuarioResultado = Usuario(resultado[0]["nombre"],resultado[0]["apellido"],resultado[0]["email"],resultado[0]["password"],resultado[0]["conf_password"])
            return usuarioResultado
        else:
            return None
    @classmethod
    def obtenerUsuario(cls,nombre):
        query = "SELECT * FROM usuarios WHERE nombre = %(nombre)s;"
        resultado = connectToMySQL("schema_magazines").query_db(query,nombre)
        return resultado

    @classmethod
    def obtenerListaUsuarios(cls):
        query = "SELECT * FROM usuarios;"
        resultado = connectToMySQL("schema_magazines").query_db(query)
        listaUsuarios=[]
        for usuario in resultado:
            listaUsuarios.append(Usuario(usuario["nombre"],usuario["apellido"],usuario["email"],usuario["password"],usuario["conf_password"]))
        return listaUsuarios

    @classmethod
    def editarUsuario(cls,usuarioAEditar):
        query = "UPDATE usuarios SET email = %(email)s, apellido = %(apellido)s WHERE nombre = %(nombre)s;"
        resultado = connectToMySQL("schema_magazines").query_db(query, usuarioAEditar)
        print(resultado)
        return resultado