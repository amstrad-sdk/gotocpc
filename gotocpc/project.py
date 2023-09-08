import configparser


def readProjectIni(file):
    config = configparser.ConfigParser()
    config.read(file)
    diccionario = {}
    for seccion in config.sections():
        diccionario[seccion] = {}
        for clave, valor in config.items(seccion):
            diccionario[seccion][clave] = valor
    return diccionario

def crear_entrada_ini(ruta_archivo, seccion, clave, valor):

    config = configparser.ConfigParser()
    config.read(ruta_archivo)
    if seccion not in config.sections():
        config.add_section(seccion)

    config.set(seccion, clave, valor)
    with open(ruta_archivo, 'w') as archivo:
        config.write(archivo)


def recorrer_claves_y_valores_ini(ruta_archivo):
    # Crear un objeto ConfigParser
    config = configparser.ConfigParser()
    
    # Leer el archivo INI
    config.read(ruta_archivo)
    
    # Recorrer las secciones del archivo INI
    for seccion in config.sections():
        # Imprimir el nombre de la sección
        print(f"[{seccion}]")
        
        # Recorrer las claves y valores de cada sección
        for clave, valor in config.items(seccion):
            print(f"{clave} = {valor}")
        
        print()  # Imprimir una línea en blanco entre secciones

# Ejemplo de uso
# ruta_archivo = "archivo.ini"
# recorrer_claves_y_valores_ini(ruta_archivo)
