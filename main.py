import os
import time

def clear_screen():
    """
    Limpia la pantalla de la terminal.
    Usa 'cls' para Windows y 'clear' para otros sistemas.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_train():
    """
    Anima un tren en movimiento de izquierda a derecha en la consola.
    """
    train = [
        "      ____      ",
        "  ___/____\\____ ",
        " /|  _  _  _  _|",
        "  |_|_|_|_|_|_| ",
        "    (O)    (O) "
    ]
    
    width = 80
    
    for position in range(0, width):
        clear_screen()
        for line in train:
            print(" " * position + line)
        time.sleep(0.1)
    print("\n¡El tren ha completado su recorrido!")

def main():
    try:
        animate_train()
    except KeyboardInterrupt:
        print("\nAnimación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
