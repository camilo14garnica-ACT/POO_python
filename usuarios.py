#    class usuario:
#    id_usuario = 1
#    documento = 1119181535
#    nombre = "Camilo"
#    apellido = "correo"
#    correo = "camilo1.0garnica@gmail.com"
#    telefono = "3224113371"
#    direccion = "calle 5a #23 21"


#CREANDO UNA INSTANCIA DE LA CLASE USUARIO

#usuario_1 = Usuarios()
#usuario_2 = Usuarios()
#print(usuario_2.nombre)
#print(usuario_1.nombre)
#print(usuario_1.correo)

#usuario_2.nombre = "Brayan"
#print(usuario_2.nombre)

lista_usuarios = [] #LITSA GLOBAL PARA ALMACENAR LA LISTA DE USUARIOS.

class Usuarios:
    #Crear una funcion para el CONSTRUCTOR
    def __init__(self,  id_usuario: int, documento, nombre, apellido, correo, telefono, direccion ): #parametros de entrada de la funcion
        self.id_usuario = id_usuario
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
    
    def saludar(self):
        print(f"hola mi nombre es {self.nombre} {self.apellido} mi dirrecion de gmail es {self.correo} y mi telefono es 📱 {self.telefono} ")
       
    # METODO CRUD 
    #CRATE / CREATE
    
    def create_usuario(self):
        lista_usuarios.append(self)
        print(f"👌 usario agregado con exito {self.nombre} ha sido registrado al sistema")
    
    #REATE / VER
    def read_usuario(self):
        print(f"ID: {self.id_usuario}, Nombre: {self.nombre}, Apellido: {self.apellido}")
        
    #UPDATE / ACTUALIZAR
    
    def update_usuarios(self, nuevo_nombre, nuevo_apellido, nuevo_telefono):
        self.nombre = nuevo_nombre
        self.apellido = nuevo_apellido
        self.telefono = nuevo_telefono
        print(f"👌 El usuario ha sido actualizado con exito a {self.nombre}{self.apellido}{self.telefono}")
    
    #DELETE /ELIMINAR
    
    def delete_usuario(self):
        if self in lista_usuarios:
            lista_usuarios.remove(self)
            print(f"👌 El usuario ha sido exitosamente {self.nombre} {self.apellido} Ha sido eliminadodel sistema")
    

 
          
       

#Creando instancia de la Clase usuario

usuario_1 = Usuarios(
    1,
    1119181535,
    "Camilo",
    "Garnica",
    "camilo1.0garnica@gmail.com",
    "3224113371",
    "calle 5a #23 21"
)

usuario_2 = Usuarios(
    2,
    123456789,
    "Luke",
    "Howland",
    "holawna1.0asda@gmail.com",
    "3221078965",
    "calle 89a #123 432")

usuario_1.saludar()
usuario_2.saludar()

#CREAR USUARIO
usuario_1.create_usuario()
usuario_2.create_usuario()
print(f"lista de usuario: {lista_usuarios}")


print(f"la lista de usuarios: {lista_usuarios[0].nombre}") #camilo
print(f"lista de usuarios {lista_usuarios[1].nombre}") # luke

usuario_1.read_usuario
usuario_2.read_usuario

        
        
