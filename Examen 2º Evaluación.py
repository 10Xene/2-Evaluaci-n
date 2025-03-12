def buscarPalabra(objetivo, palabras):

    
    # Para cada nombre de los nombres
    for nombre in nombres:
        # Si el nombre es igual al objetivo
        if nombre == objetivo:
            nombre ==nombre



nombres=["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
for nombre in nombres:
        # Si nombre está en nombres
        if nombre in nombres:
            print(f"{nombre} está en la lista de nombres.")
        else:
            print(f"{nombre} no está en la lista de nombres.")
            
def imprimirEdades(edades):
    for nombre, edad in edades.items():
        print(f"{nombre} tiene {edad} años.")
    print(buscarPalabra("EXIT", nombres))
    
    def imprimirListaInversa(lista):
        lista = lista[::-1]
        return lista
    
    print(imprimirListaInversa(""))