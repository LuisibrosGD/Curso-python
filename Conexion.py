import mysql.connector

class CConexion:
    
    def ConexionBaseDeDatos(self):
        try:
            conexion = mysql.connector.connect(
                user = 'root',
                password = 'mondongo',
                host = '127.0.0.1',
                database = 'clientes_db',
                port = '3306'
            )
            
            print("Conexion correcta")
            
            return conexion
            
        except mysql.connector.Error as error:
            print(f"Error al conectarte a la base de datos {error}")
            
            return conexion

objeto1 = CConexion()
objeto1.ConexionBaseDeDatos()