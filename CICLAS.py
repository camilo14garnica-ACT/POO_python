#CREAMOS UNA LISTA VACIA PARA GUARDAR LAS CICLAS QUE VAMOS A REGISTRAR
#CREAMOS LA CLASE PADRE
lista_ciclas = []
class Cicla:


#Crear una funcion para el CONSTRUCTOR
    def __init__(self, ID_cicla: int, Serial, Marca, Modelo, Tipo, color, Dueño):
        self.ID_cicla = ID_cicla
        self.serial =  Serial
        self.Marca = Marca
        self.modelo = Modelo
        self.tipo = Tipo
        self.color = color
        self.dueño = Dueño
        
    def encriptar_serial(self,Serial):
        print(f"Serial encriptado: {Serial}")
        
    #metodo base CRUD
    
    #Create
    def create_usuario(self):
        lista_ciclas.append(self)
        print(f"👌cicla agregada con exito Marca: {self.Marca}, Dueño: {self.dueño}")
    
    #READ
    def read_ciclas(self):
        print(f"lista de ciclas ID: {self.ID_cicla} Marca: {self.Marca} Dueño: {self.dueño}")
        
    #UPDATE
    def update_cicla(self, ID_nuevo, Serial_nuevo, Marca_nueva):
        self.ID_cicla = ID_nuevo
        self.serial = Serial_nuevo
        self.Marca = Marca_nueva
        print(f"👌 La cicla ha sido actualizada correctamente {self.ID_cicla} {self.serial} {self.Marca}")
    
    #DELETE
    def delete_cicla(self):
        if self in lista_ciclas:
            lista_ciclas.remove(self)
            print(f"👌La cicla {self.ID_cicla} {self.Marca} ha sido eliminado correctamente")
        else:
            print(f"⚠️: La cicla {self.ID_cicla} no se encuentra registrada en el sistema.")   
    
    #METODO PARA VENDER
    def vender_cicla(self):
        print(f"La cicla {self.Marca} se ha vendido exitosamente👌") 

#Creamos una instancia dela clase CICLA

cicla_1 = Cicla(1, 12345, "Colnago", "UCI_Tour", "Ruta", "Blanco", "Pogacar")

cicla_2 = Cicla(2, 678910, "BMW", "vuelta-colombia", "Ruta", "Negra", "Camilo" )

cicla_3 = Cicla(3, 1357890, "Trek", "TOUR_uci", "Gravel", "Verde", "Sharyt")

#llamar los metodos CREATE

print("=" * 100)
print(f"METODO DE CREAR")
print(f"lista de ciclas: {lista_ciclas}")
cicla_1.create_usuario()
cicla_2.create_usuario()
cicla_3.create_usuario()


print("=" * 100)
#Llamar los metodos READ
print("METODO PARA LEER")
cicla_1.read_ciclas()
cicla_2.read_ciclas()
cicla_3.read_ciclas()

#ver los metodos UPDATE
print("=" * 100)
print("METODO PARA ACTUALIZAT LOS DATOS")
cicla_1.update_cicla(1, 12345, "Masterclass")
cicla_2.update_cicla(2, 678910, "BMW_SPORT")
cicla_3.update_cicla(3, 1357890, "Trek_ELITE")

#llamar los metodos DELETE

print("=" * 100)
print("METODO PARA ELIMINAR DATOS")
cicla_1.delete_cicla()

#llamar el metodos para vender 
print("=" * 100)
print("METODO PARA VENDER")
cicla_3.vender_cicla()




print("=" * 100)
print("APLICANDO LOS 4 PILARES DE LA PROGRAMACION (POO)")
print("HERENCIA Y CAPSULAMINETO")
#-------------------------------------------
#APLICANDO LOS 4 PILARES DEL POO
#-------------------------------------------

#HERENCIA Y ENCAPSULAMIENTO CICLA

class montaña(Cicla):
    def __init__(self,ID_cicla: int, Serial, Marca, Modelo, Tipo, color, Dueño, suspension, freno_disco, precio=[] ):
        
        # Usamos super() para llamar al constructor de la clase padre (Usuario)
        super().__init__(ID_cicla, Serial, Marca, Modelo, Tipo, color, Dueño)
        
        #Atributos propios de la 
        
        self.__suspension = suspension
        self.__precio = precio
        self.__freno_disco = freno_disco
        
        #ENCAPSULAMIENTO: Usamos un atributo privado para almacenar los valores
        # La suspensión y el precia, la suspension quedando como un atributo privado.
        
    #GET >consultar o ver el atributo
    def get_suspension(self):
        return self.__suspension
    
    #SET >para modificar o actualiazar el atributo
    def set_precio(self, nuevo_precio):
        self.__precio.append(nuevo_precio)
        print(f"Nuevo precio guardado para la {self.ID_cicla}. Total precio: {len(self.__precio)}")
    
        
    #4. POLIMORFISMO
    # Sobrescribimos el metodo de la clase padre para darle un comportamiento en especifico
    
    def consultar_precio(self):
        print(f"👌[VALOR DE LA CICLA] Obteniendo precio de la cicla {self.Marca} de modelo {self.modelo}, con suspesnion de {self.__suspension} con un valor de, {self.__precio}")
        
cicla_1 = montaña(1, 12345, "clif", "UCI_tour", "tipo", "Negro", "Camilo", "airforce", "freno_disco", 5234897)

print(f"Imprimir atributo privado {cicla_1.get_suspension()}")
print(f"Imprimir atributo publico {cicla_1.serial}")
print("=" * 100)







class ruta(Cicla):
    def __init__(self,ID_cicla: int, Serial, Marca, Modelo, Tipo, color, Dueño, peso, cadencia, precio=[]):
        super().__init__(ID_cicla, Serial, Marca, Modelo, Tipo, color, Dueño)
        self.peso = peso
        self.cadencia = cadencia
        self.precio = precio
        
    # 4. POLIMORFISMO
    def consultar_precio(self):
        print(f"👌[VALOR DE LA CICLA] Obteniendo precio de la cicla {self.ID_cicla}, de modelo {self.modelo}, peso {self.peso} kg, con un valor de, {self.precio}")
        
        
# Crear una instancia de ruta para usar el método consultar_peso
cicla_gravel = ruta(99, "1119181535", "Pinarrelo", "Colombian-tour", "Gravel", "negro", "Camilo_Orduz", 12.5, 90, 3221495 )



cicla_1.consultar_precio()
cicla_gravel.consultar_precio()




