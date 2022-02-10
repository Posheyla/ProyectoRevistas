from revistas_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from revistas_app.modelos.modelo_usuarios import Usuario

class Revista:
    def __init__(self,id,autor,titulo,contenido,usuario_email):
        self.id=id
        self.autor = autor
        self.titulo = titulo
        self.contenido = contenido
        self.usuario_email = usuario_email

    @classmethod
    def agregarRevista(cls,nuevaRevista):
        query = "INSERT INTO revistas(autor,titulo,contenido,usuario_email) VALUES(%(autor)s,%(titulo)s,%(contenido)s,%(usuario_email)s)"
        resultado = connectToMySQL("schema_magazines").query_db(query,nuevaRevista)
        return resultado

    @classmethod
    def desplegarRevistas(cls,autor):
        query = "SELECT * FROM revistas WHERE autor = %(autor)s;"
        resultado = connectToMySQL("schema_magazines").query_db(query,autor)
        listaRevistas = []
        for revista in resultado:
            listaRevistas.append(cls(revista["id"],revista["autor"],revista["titulo"],revista["contenido"],revista["usuario_email"]))
        return listaRevistas

    @classmethod
    def obtenerListaDeMagazinesConUsuarios(cls):
        query = "SELECT * FROM revistas m LEFT JOIN usuarios u ON m.usuario_email = u.email;"
        resultado = connectToMySQL("schema_magazines").query_db(query)
        listaRevistasConUsuario=[]
        for renglon in resultado:
            listaRevistasConUsuario.append(cls(renglon["id"],renglon["autor"],renglon["titulo"],renglon["contenido"],renglon["usuario_email"]))
        return listaRevistasConUsuario  

    @classmethod
    def obtenerRevista(cls,id):
        query = "SELECT * FROM revistas WHERE id = %(id)s;"
        resultado = connectToMySQL("schema_magazines").query_db(query,id)
        return resultado

    @classmethod
    def eliminarRevista(cls, id):
        query = "DELETE FROM revistas WHERE id = %(id)s;"
        resultado =connectToMySQL("schema_magazines").query_db(query,id)
        return resultado
        
