# 1) Richiesta del numero intero positivo
n = int(input("Inserisci un numero intero positivo: "))
while n <= 0:
    print("Numero non valido. Riprova.")
    n = int(input("Inserisci un numero intero positivo: "))

# 2) Menù a scelta ripetibile
while True:
    print("\n--- MENU ---")
    print("1) Somma dei numeri pari da 1 a n")
    print("2) Stampa dei numeri dispari da 1 a n")
    print("3) Verifica se n è primo")
    print("4) Esci")
    scelta = int(input("Scegli un'opzione (1-4): "))

    if scelta == 1:
        # Calcolo e stampa della somma dei numeri pari da 1 a n
        somma_pari = 0
        for i in range(1, n + 1):
            if i % 2 == 0:
                somma_pari += i
        print("La somma dei numeri pari tra 1 e", n, "è:", somma_pari)

    elif scelta == 2:
        # Stampa di tutti i numeri dispari da 1 a n
        print("Numeri dispari da 1 a", n, ":")
        for i in range(1, n + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print()  # Va a capo

    elif scelta == 3:
        # Verifica se n è primo (divisibile solo per 1 e se stesso)
        if n < 2:
            print(n, "non è un numero primo.")
        else:
            e_primo = True
            for i in range(2, n):
                if n % i == 0:
                    e_primo = False
                    break
            if e_primo:
                print(n, "è un numero primo.")
            else:
                print(n, "non è un numero primo.")

    elif scelta == 4:
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida. Riprova.")
