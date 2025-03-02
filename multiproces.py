from multiprocessing import Process
import time
import os


def contar(num):
    iter = 0
    while iter < num:
        iter += 1


def main():
    num = 100000000
    print("--- Se inicio el conteo ---")
    start = time.perf_counter()
    thread1 = Process(target=contar, args=[num / 2])
    thread2 = Process(target=contar, args=[num / 2])
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end = time.perf_counter()
    print("--- Finalizo el conteo ---")
    print(f"--- Tiempo de demora : {end - start} ---")

if __name__ == "__main__":
    os.system("cls")
    main()