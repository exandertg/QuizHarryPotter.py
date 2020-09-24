#Proyecto: Quiz Harry Potter
#Aurot: Alexander Tzoc Guarchaj
#Carnet: 2262015      
#Autor:
#Carnet:
#Este programa le pedirá al usuario que responda un Quiz

#Llamar todas las dunciones que se necesitan
from random import randint
from time import sleep
from screen import clear

#El programa saludará al usuario
print ("Bienvenido al Quiz de Harry Potter")
print ("Veamos cuanto sabes sobre la mejor saga de Magia y Hechicería")

#Pedir al usuario que ingrese su numbre y su genero
nombre = input ("Ingresa tu nombre: ")
genero= input ("Ingrese su genero: ")
input ("Presiona enter para iniciar con las preguntas")
clear ()
sleep (5)

#Declaración de variables
puntos = 0

#El ciclo while servirá para realizar las preguntas y contabilizar los puntos
#El ciclo if y elif servirán para tomar una desicón y atribuirle los puntos 
#A la respuesta que el usuario ingreso
while True:

    print ("""
    1. ¿Dónde vivía Harry y la familia Dursley?

    a. Londres
    b. Oxford Street
    c. Privet Driv """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()

    print ("""
    2. ¿Cúal fue la casa de Bellatrix Lestrange cuando estudió en Hogwarts?

    a. Gryffindor
    b. Ravenclaw
    c. Slytherin """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear () 

    print ("""
    3. Snape es un mago muy poderoso que invento un montón de hechizos.
    ¿Cúal de éstos es suyo ?

    a. Sectumsempra
    b. Serpensortia
    c. Lumos """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()

    print ("""
    4. Tras la muerte de Dumbledore... 
    ¿Quién se convirtió dueño de la poderosa varita de sauco?

    a. Harry Potter
    b. Draco Malfoy
    c. Severus Snape """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    5. ¿Quién es Merope Gaunt?

    a. Una miembro de la Orden del Fenix
    b. La madre de Voldemort
    c. La fundadora de Hawarts """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()

    print ("""
    6. ¿Cómo se llama el hermano mayor de la familia Weasley?

    a. Fred
    b. Percy
    c. Bill """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()

    print ("""
    7. ¿Cómo se llama la mamá de Hagrid?

    a. Arabella
    b. Maxine
    c. Fridwulfa """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    8. ¿Qué regalo de sus amos hace libre a los Elfos domésticos?

    a. Un anillo
    b. Una prenda de Vestir
    c. Un hechizo """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    9. ¿A qué se dedicaban los padres de Hermione?

    a. Abogados
    b. Profesores
    c. Dentistas """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    10. ¿Quién le entrega la capa de invisibilidad a Harry Potter?

    a. Hagrid
    b. Dumbledore
    c. Sirius Black """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    11. ¿Cómo se llama la profesora que enseñaba adivinación en Hogwarts?

    a. Sinistra
    b. Minerva
    c. Sybil """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    12. ¿Cúal es el hechizo para ahuyentar a los dementores?

    a. Expecto Patronum
    b. Expelliarmus
    c. Sectumsempra """)

    categoria = input ("Elige una categoria: ")

    if categoria == "a" or categoria == "A":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    13. ¿Qué sabores de caramelos Bertie Bott's le toca a
    Dumbledore en la enfermería?

    a. Vómito
    b. Moco
    c. Cera de Oído """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()
    
    print ("""
    14. ¿Cuál de los volúmenes es el libro más 
    rápidamente vendido de la historia?

    a. El prisionero de Azkaban
    b. Las reliquias de la muerte 
    c. El cáliz de fuego """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Sus puntos actuales son:", puntos)
    input ("Presiona Enter para pasar a la sigueinte pregunta :D")
    clear ()

    print ("""
    15. ¿Qué fué lo que hizo Harry para burlar al Colacuerno Húngaro?

    a. Uso su saeta de fuego 
    b. Uso expelliarmus
    c. Uso una bómba fetida """)

    categoria = input ("Elige una categoria ente a,b o c: ")

    if categoria == "a" or categoria == "A":
        puntos += + 3
        print ("La respuesta es correcta")
        print ("Felicidades llegó al final del juego")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "b" or categoria == "B":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Felicidades llegó al final del juego")
        print ("Sus puntos actuales son:", puntos)
    elif categoria == "c" or categoria == "C":
        puntos += + 1
        print ("La respuesta es incorrecta")
        print ("Felicidades llegó al final del juego")
        print ("Sus puntos actuales son:", puntos)
        input ("Presiona Enter para ver sus resultados finales")
        clear ()
    if puntos <= 13 :
        print (puntos)
        print ("Eres un simple Muugle :(")
    elif puntos <= 25 :
        print (puntos)
        print ("Eres un Muggle Sangre Sucia :/")
    elif puntos <= 35:
        print (puntos)
        print ("Eres un Mago Sangre Mestiza :)")
    elif puntos <= 45:
        print (puntos)
        print ("Eres un Mago Sangre Pura :D")
        clear ()
    break
print ("¡Gracias por participar!")
input ()