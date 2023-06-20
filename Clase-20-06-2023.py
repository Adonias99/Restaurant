
lista_rut = []

Coca = 1500
Mojito = 4000
Vino = 2500

Huevo_con_patatas = 5500
Bistec_con_pure = 7000
Curanto_al_hoyo = 9500

Cheesecake = 5000
Miloja = 3000
Jalea = 2000

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in (1,2,3,4,5,6):
                return opcion
            else:
                print("ERROR! debe ingresar una opción de 1 a 6! ")
        except:
            print("ERROR! debe ingresar un número entero!")  

            if opcion == 1:
                pass
            elif opcion == 2:
                reservar_mesa()
        
            elif opcion ==3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            else:
                break
            


def ver_restaurant():
    pass

def reservar_mesa():
    rut = validar_rut
    nombre = validar_nombre
    correo = validar_correo  
    cantidad = validar_reserva 

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3:
            return nombre

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su Rut:"))    
            if rut >= 1000000 and rut <= 99999999:
                lista_rut.append[rut]
                return rut
            else:
                print("ERROR! debe ingresar un rut valido entre 1.000.000 y 99.999.999")
        except:
            print("ERROR! debe ingresar un número entero!")        

def validar_correo():
    correo = input("Ingrese su correo: ")
    if "@" in correo:
        return correo
    
def validar_reserva():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de personas que asisten: "))
            if cantidad >= 1 and cantidad <=6:
                return cantidad
            else:
                print("ERROR! debe ingresar un número entre 1 y 6!")
        except:
            print("ERROR 1 debe ingresar un número entero!")        
    
def validar_carta():
    rut = validar_rut
    for x in lista_rut:
        for x in range (len(lista_rut)):
            if rut == lista_rut:
                validar_alimentos()
                opcion = opcion_alimentos
                
            else:
                print("ERROR! este rut no se encuentra en nuestra lista de asistentes, ingrese uno valido")

def validar_alimentos():
    while True:
        print("""Menú Alimentos
        1. Bebestibles
        2. Platos
        3. Postres
        4. Pedir
        5. Cancelar""")

def opcion_alimentos():
        while True:
            try:
                opcion = int(input("Ingrese opción: "))
                if opcion in (1,2,3,4,5):
                    return opcion
                else:
                    print("ERROR! debe ingresar una opción de 1 a 5! ")
            except:
                print("ERROR! debe ingresar un número entero!") 



def carta():
    rut = validar_carta
    validar_alimentos()

    

def validar_pagar():
    pass


        
            



while True:
    print("""Menú
    1. Ver Restaurant
    2. Reservar Mesa
    3. Carta
    4. Pagar
    5. Cancelar
    6. Salir""")

    opcion = validar_opcion()
   
    


