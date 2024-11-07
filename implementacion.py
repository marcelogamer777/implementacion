import random

def lanzar_dado():
    return random.randint(1, 6)

def main():
    print("¡Bienvenido al simulador de lanzamiento de dados!")
    contador = {suma: 0 for suma in range(2, 13)}
    
    while True:
        lanzar = input("¿Desea lanzar los dados? (s/n): ").lower()
        if lanzar == 'n':
            break
        
        dado1 = lanzar_dado()
        dado2 = lanzar_dado()
        suma = dado1 + dado2
        contador[suma] += 1
        
        print(f"Resultado del lanzamiento: {dado1} + {dado2} = {suma}")
    
    print("\nEstadísticas de los lanzamientos:")
    for suma, veces in contador.items():
        print(f"Suma {suma}: {veces} veces")
    
if __name__ == "__main__":
    main()
