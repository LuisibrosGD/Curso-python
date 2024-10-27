from Conexion import *

class CClientes:
    
    def mostrarClientes(self):
        try:
            cone = CConexion.ConexionBaseDeDatos(self)
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM usuarios;")
            
            miResultado = cursor.fetchall()
            
            cone.commit()
            cone.close()
            return miResultado
            
        except mysql.connector.Error as error:
            print(f"Error de mostrar datos {error}")




    def ingresarClientes(self,nombres,apellidos,sexo):
        
        try:
            cone = CConexion.ConexionBaseDeDatos(self)
            cursor = cone.cursor()
            sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s);"
            # La variable valores tiene que ser una tupla
            # Como mínima expresión es: (valor,) la coma hace que sea una tupla
            # Las tuplas son listas inmutables
            valores = (nombres,apellidos,sexo)
            cursor.execute(sql,valores)
            cone.commit()
            
            cursor.close()
            cone.close()
            #Le mandamos un mensaje
            print(cursor.rowcount,"Registro ingresado")
            
        except mysql.connector.Error as error:
            print(f"Error de ingreso de datos {error}")
        