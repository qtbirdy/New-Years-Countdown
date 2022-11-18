import os
from time import sleep
import urllib.request

def hack_program():
    print("\n\n\n\n ============  Hacking ========== \n\n\n\n\n 💀💀💀")
    n = 10
    sleep(1)
    while n > 0:
        print(n)
        print(["💀"] * n)
        sleep(0.05)
        n -= 1
        
    print("Thanks for sharing your computer information ....")
    sleep(0.5)
    for key, value in os.environ.items():
        print(f"{key} ****** {value}")
        sleep(0.03)

    print("\n\n\n\n\nThank you so much! Here's a little gift in exchange...\n\n\n")
    sleep(0.3)
    input_number = input("How many gifts do you want?")
    for i in range(int(input_number)):
        urllib.request.urlretrieve("https://media.istockphoto.com/id/1267466399/es/foto/perro-cachorro-feliz-sonriendo-sobre-fondo-amarillo-aislado.jpg?s=1024x1024&w=is&k=20&c=couAZEjDn-N7WdssiAG-3IPntE02f1H_UAafgJnD9h0=", f"don't open {i}.jpg")

    print("Voila:", ["💣"] * int(input_number))

if __name__ == "__main__":
    hack_program()