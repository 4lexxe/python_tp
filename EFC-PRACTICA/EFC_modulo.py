def cambiar_vocal(cad, letra):
    lista_cad = cad.split(" ")
    cad_nueva = []
    for palabra in lista_cad:
        if letra in palabra:
            palabra = palabra.replace(letra, letra.upper())
        cad_nueva.append(palabra)
        
    cad_nueva = " ".join(cad_nueva)
    
    print(f"Cadena original: {cad}")
    print(f"Cadena nueva: {cad_nueva}")
    
cambiar_vocal("Roses are red violets are blue sugar is sweet and so are you", "e")