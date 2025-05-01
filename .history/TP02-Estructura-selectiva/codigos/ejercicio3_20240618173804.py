"""3. Analice el siguiente código en Python:
1. clave = "iprog1"
2. contraseña = input("Introduce la contraseña: ")
3. if clave == contraseña:
4. print("La contraseña coincide")
5. else:
6. print("La contraseña NO coincide")
● ¿Cuándo se visualizará en la pantalla el mensaje “coincide”?
● Si ingresa en la variable contraseña iProg1, ¿Qué mensaje se verá en la pantalla?
● Mejore la sentencia en la línea 3 utilizando alguna función que salve la situación anterior.
● ¿Qué sucede si ingresa un número?"""

clave = "iprog1"
contraseña = input("Introduce la contraseña: ")

if clave == contraseña.lower():
    print("La contraseña coincide")
else:
    print("La contraseña NO coincide")