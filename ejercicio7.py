"""userReply = input("¿Necesita enviar un paquete?(Ingrese sí o no)")
if userReply == "si":
    print("Podemos ayudarlo a enviar ese paquete!")
else:
    print("Vuelve cuando necesites enviar un paquete. Gracias.")
"""
userReply = input("¿Le gustaría comprar estampillas, comprar un sobre o hacer una copia? (Ingrese sellos, sobre o copia)")
if userReply == "sellos":
    print("Tenemos muchos diseños de sellos para elegir.")
elif userReply == "sobre":
    print("Tenemos muchos tamaños de sobres para elegir.")
elif userReply == "copia":
    copias = input("¿Cuántas copias quieres? (Ingrese un numero)")
    print("Aquí hay {} copias".format (copias))
else:
    print("Gracias, por favor venga de nuevo.")
    