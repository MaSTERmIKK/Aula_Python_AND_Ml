# utente = ["mirko", 21, True ]

# cap = int(input("inserisci il tuo cap"))

# utente.append(cap)

# lista_utenti = []

# lista_utenti.append(utente)

# utente = ["marco", 24, False, 10022 ]

# lista_utenti.append(utente)

# print(lista_utenti)

# print(len(lista_utenti))

# id = len(lista_utenti)

# utente = lista_utenti[0]

# lista_utenti=[]
# id = 0

# aggiunte= int(input("quanti utenti vuoi aggiungere"))

# while(len(lista_utenti )<=aggiunte):
#     utente2=[]
#     nome = input("isnerisci il tuo nome")
#     utente2.append(nome)
#     password = input("isnerisci la password")
#     utente2.append(password)
#     id +=1
#     utente2.append(id)
    
#     lista_utenti.append(utente2)
#     print(utente2)
#     print(lista_utenti)
    
# print(lista_utenti)


# creare un sistema di if che al rispetto di certe condizioni predefinite
# aggiunga i valori corrispondenti ad una lista, in ordine crescente

lista_valori=[]

valore1 = int(input("aggiungi valore numerico"))
valore2 = int(input("aggiungi valore numerico"))
valore3 = int(input("aggiungi valore numerico"))

if valore1 > 0 and valore2 > 0 and valore3 >0 :
    lista_valori.append(valore2)
    lista_valori.append(valore1)
    lista_valori.append(valore3)
    
    if len(lista_valori) > 0 :
        lista_valori.sort()
        print(lista_valori)
        

numeroValori = int(input("quanti valori vuoi aggiungere?"))
lista_valori2=[]

while len(lista_valori2)<=numeroValori:
    valore = int(input("quale valore vuoi aggiungere?"))
    lista_valori2.append(valore)
    print(lista_valori2)
    
lista_valori2.sort()
lista_valori2.reverse()
print(lista_valori2)