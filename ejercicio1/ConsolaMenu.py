from Usuario import Usuario

class ConsolaMenu:
    
    def mostrarMenu(self):
        while(True):
            print("SISTEMA DE GESTION DE CLIENTES")
            print("1. Agregar usuario")
            print("2. Eliminar usuario")
            print("3. Buscar usuario")
            print("4. Modificar datos de usuario")
            print("5. Ver todos los usuarios")
            print("0. Salir")
            try:
                opcion = int(input("Ingrese su opcion: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
            if opcion == 1:
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                edad = int(input("Ingrese edad: "))
                persona = Usuario(nombre,apellido,edad)
                persona.agregarUsuario()
            elif opcion == 2:
                
                index = int(input("Ingrese el id del usuario a eliminar: "))
                persona = Usuario(None,None,None)
                persona.eliminarUsuario(index)
                
            elif opcion == 3:
                persona = Usuario(None,None,None)
                
                indice = int(input("Ingrese el id del usuario: "))
                persona.buscarUsuarioOpcion(indice)
            
            elif opcion == 4:
                print("modificar datos usuario")
                persona = Usuario(None,None,None)
                persona.actualizarUsuario()
            elif opcion == 5:
                persona = Usuario(None,None,None)
                persona.mostrarUsuarios()
            elif opcion == 0:
                print("Saliendo del programa")
                break    
            else:
                print("Opcion invalida")
    