import mysql.connector

class Usuario:
    def __init__(self, nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    @staticmethod
    def conectar_db():
        return mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'mondongo',
            database = 'usuarios_db'
        )
        
    def agregarUsuario(self):
        db = self.conectar_db()
        cursor = db.cursor()
        sentencia_sql = 'INSERT INTO persona(nombre, apellido, edad) VALUES (%s,%s,%s)'
        valores = (self.nombre,self.apellido,self.edad)
        cursor.execute(sentencia_sql,valores)
        db.commit()
        
        cursor.close()
        db.close()
    
    def eliminarUsuario(self, id_usuario):
        db = self.conectar_db()
        cursor = db.cursor()
        resultado = self.buscarUsuario(id_usuario)
        if resultado:
            print(f'ID: {id_usuario}\nNombre: {resultado[0]}\nApellido: {resultado[1]}\nEdad: {resultado[2]}')
            print("--------------------")
            opcion = input("Desea eliminar este usuario? (1 = Si, 0 = No): ")
            if opcion == '0':
                print("Opción cancelada. Regresando al menú principal")
            elif opcion == '1':
                sentencia_sql = 'DELETE FROM persona WHERE id = %s'
                cursor.execute(sentencia_sql, (id_usuario,))
                db.commit()
                print(f'SE HA ELIMINADO EL REGISTRO:\nID: {id_usuario}\nNombre: {resultado[1]}')
            else:
                print("Opción inválida.")
        else:
            print("Usuario no encontrado.")
        
        del resultado
        
        cursor.close()
        db.close()
    
    def actualizarUsuario(self):
        db = self.conectar_db()
        cursor = db.cursor()
        
        #Buscar el usuario a actualizar
        id_usuario = int(input("Ingrese el id del usuario"))
        resultado = self.buscarUsuario(id_usuario)
        if resultado is not None:
            print(f'ID: {id_usuario}\nNombre: {resultado[0]}\nApellido: {resultado[1]}\nEdad: {resultado[2]}')
            print("--------------------")
        else:
            print(f"No se encontro el registro de ID = {id_usuario}")
            
        while(True):
            print("Actualizar")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("0. Volver")
            opcion = int(input("Digite su opcion: "))
            
            if opcion == 1:
                campo = "nombre"
                dato_modificar = input("Ingrese el nuevo nombre: ")
                
            elif opcion == 2:
                campo = "apellido"
                dato_modificar = input("Ingrese el nuevo apellido: ")
                
            elif opcion == 3:
                campo = "edad"
                dato_modificar = int(input("Ingrese la nueva edad: "))
            elif opcion == 0:
                print("Volviendo al menu principal")
                break
            else:
                print("opcion invalida")
            
            sentencia_sql = f'UPDATE persona SET {campo} = %s WHERE id = %s'
            valores = (dato_modificar, id_usuario)

            cursor.execute(sentencia_sql,valores)
            db.commit()
            print(f"Se ha actualizado '{resultado[opcion]}' por '{dato_modificar}'")
            cursor.close()
            db.close()
            
            
            
    
    def buscarUsuario(self, id_usuario):
        db = self.conectar_db()
        cursor = db.cursor()
        sentencia_sql = 'SELECT * FROM persona WHERE id = %s'
        valores = (id_usuario,)
        cursor.execute(sentencia_sql, valores)
        resultado = cursor.fetchone()  # Devuelve una sola tupla o None si no existe
        cursor.close()
        db.close()
        return resultado
    
    def mostrarUsuarios(self):
        db = self.conectar_db()
        cursor = db.cursor()
        sentencia_sql = 'SELECT * FROM persona'
        
        cursor.execute(sentencia_sql)
        resultado = cursor.fetchall()
        
        for persona in resultado:
            print(f"ID: {persona[0]}")
            print(f"Nombre: {persona[1]}")
            print(f"Apellido: {persona[2]}")
            print(f"Edad: {persona[3]}")
            print("-------------------")
        
        cursor.close()
        db.close()
    
    def buscarUsuarioOpcion(self, index):
        db = self.conectar_db()
        cursor = db.cursor()
        sentencia_sql = 'SELECT * FROM persona WHERE id = %s'
        valores = (index,)
        cursor.execute(sentencia_sql, valores)
        resultado = cursor.fetchone()  # Devuelve una sola tupla o None si no existe
        
        if resultado is None:
            print("No hay resultados")
        else:
            print(f'ID: {resultado[0]}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nEdad: {resultado[3]}')
            print("--------------")
        cursor.close()
        db.close()
    