videojuegos = {
    'GOW001': ['God of War', 'PS5', 'Aventura', 'M', 'Santa Monica Studio', 2022, 'Sony'],
    'ZEL002': ['The Legend of Zelda: Tears of the Kingdom', 'Switch', 'Aventura', 'E10+', 'Nintendo', 2023, 'Nintendo'],
    'ELD003': ['Elden Ring', 'Multiplataforma', 'RPG', 'M', 'FromSoftware', 2022, 'Bandai Namco'],
    'SPD004': ['Spider-Man 2', 'PS5', 'Acción-Aventura', 'T', 'Insomniac Games', 2023, 'Sony'],
    'MNC005': ['Minecraft', 'Multiplataforma', 'Sandbox', 'E', 'Mojang', 2011, 'Microsoft'],
    'FNF006': ['Five Nights at Freddy’s: Security Breach', 'Multiplataforma', 'Terror', 'T', 'Steel Wool Studios', 2021, 'ScottGames'],
    'GT7007': ['Gran Turismo 7', 'PS5', 'Carreras', 'E', 'Polyphony Digital', 2022, 'Sony'],
    'HLY008': ['Hogwarts Legacy', 'Multiplataforma', 'RPG', 'T', 'Avalanche Software', 2023, 'Warner Bros']
}

stock = {
    'GOW001': [59_990, 12],
    'ZEL002': [69_990, 8],
    'ELD003': [49_990, 15],
    'SPD004': [64_990, 5],
    'MNC005': [19_990, 30],
    'FNF006': [34_990, 7],
    'GT7007': [54_990, 10],
    'HLY008': [59_990, 6]
}


def buscar_juego_por_nombre(nombre_juego:str):
    for i in videojuegos:
        #print(videojuegos[i][0])
        if videojuegos[i][0].lower() == nombre_juego.lower():
            print("Encontrado!!")
            juego_encontrado = videojuegos[i]
            juego_encontrado.insert(0,i)
            return juego_encontrado


#print(buscar_juego_por_nombre("god of "))

def buscar_stock_por_codigo(codigo_juego:str):
    for i in stock:
        if i.lower() == codigo_juego.lower():
            #print("encontrado!!")
            return stock[i][1]
        #print(stock[i][1])


#print(buscar_stock_por_codigo("gow001"))



def disminuir_stock(codigo_juego:str,cantidad:int):
    stock_disponible = buscar_stock_por_codigo(codigo_juego)
    #       12                  60
    if stock_disponible >= cantidad:
        stock[codigo_juego.upper()][1] -= cantidad
        return True
    else:
        return False


#print(disminuir_stock("ZEL00a2",8))
#print(stock)


def mostrar_todos_los_juegos():
    for i in videojuegos:
        print(f"NOMBRE: {videojuegos[i][0]}  ||  PLATAFORMA:  {videojuegos[i][1]}")


#mostrar_todos_los_juegos()



def actualizar_precio_juego(nombre_juego:str, precio_nuevo:int):
    juego_encontrado = buscar_juego_por_nombre(nombre_juego)
    if juego_encontrado != None:
        print(juego_encontrado)
        for i in stock:
            if i.upper() ==  juego_encontrado[0].upper():
                stock[i][0] = precio_nuevo
    else:
        print("El juego no se encontro!!!")
                



#actualizar_precio_juego("minecraft",490)
#print(stock)


def buscar_juego_por_anio(rango_minimo:int, rango_maximo:int):
    for i in videojuegos:
        if videojuegos[i][5] >= rango_minimo and videojuegos[i][5] <= rango_maximo:
            print(videojuegos[i])




#buscar_juego_por_anio(2021,2021)




def valida_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto


#print(valida_texto("ingrese una opcion: "))





def valida_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("No puede ingresar valores negativos o directamente 0.")
                continue
            else:
                return numero
        except ValueError:
            print("Solo se pueden ingresar nuemros enteros.")
            continue


def menu():
    print("===== TIENDA DE VIDEOJUEGOS =====")
    while True:
        print("1. Vender juego")
        print("2. Mostrar todos los juegos")
        print("3. Actualizar precio de un juego")
        print("4. Filtrar juegos por año de lanzamiento")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opcion:"))
        except ValueError:
            print("Solo se permiten valores numericos.")


        if opcion == 1:
            codigo_juego = valida_texto("Ingrese el codio del juego: ")
            cantidad_comprar = valida_numero_entero_positivo("Ingrese la cantidad a comprar: ")
            compra = disminuir_stock(codigo_juego,cantidad_comprar)
            if compra == True:
                print("Compra realizada con exito!")
            else:
                print("No hay stock disponible!")
        elif opcion == 2:
            mostrar_todos_los_juegos()
        elif opcion == 3:
            nombre_juego = valida_texto("Ingrese el nombre del juego: ")
            nuevo_precio = valida_numero_entero_positivo("Ingrese el nuevo precio del juego: ")
            actualizar_precio_juego(nombre_juego,nuevo_precio)
        elif opcion == 4:
            rango_minimo = valida_numero_entero_positivo("Ingrese el rango minimo: ")
            rango_maximo = valida_numero_entero_positivo("Ingrese el rango maximo: ")
            buscar_juego_por_anio(rango_minimo, rango_maximo)
        elif opcion == 5:
            break
        else:
            print("Opcion no valida - [1-5]")



menu()



