# EJEMPLO DE UN CODIGO SIMULANDO LA PROGRAMACION CONCURRENTE CON HILOS #

import os
from threading import Thread
import time

biblioteca = ["titanic", "la monga"]
menu_estado = 0

def menu():
    os.system("cls")
    print("Menu:\n")
    print("1.- Mostrar Biblioteca\n2.- Descargar Pelicula\n3.- Salir")

def mostrar_biblioteca():
    os.system("cls")
    print("Peliculas: \n")
    for pelicula in biblioteca: print(pelicula)

def descargar_pelicula(pelicula):
    print(f".......Descargando {pelicula}.......")
    time.sleep(7)
    print(f"\n{pelicula} Descargada Correctamente")
    biblioteca.append(pelicula)

def actualizar_biblioteca(hilo):
    hilo.join()
    if menu_estado == 1: mostrar_biblioteca()
    input("\nEnter para continuar")

while True:
    os.system("cls")
    menu_estado = 0
    menu()
    opcion = input("Seleccione una Opciones: ")
    if opcion == "1":
        os.system("cls")
        menu_estado = 1
        print("---Biblioteca---\n")
        mostrar_biblioteca()
        input("\nEnter para continuar")

    elif opcion == "2":
        os.system("cls")
        menu_estado = 2
        print("Colcoa el nombre de la pelicula que quiereas descargar")
        hilo1 = Thread(target=descargar_pelicula, args=[input("Nombre: ")])
        hilo2 = Thread(target=actualizar_biblioteca, args=[hilo1])
        hilo1.start()
        hilo2.start()
        input("\nEnter para continuar")

    else:
        os.system("cls")
        print("Se salio del programa")
        break