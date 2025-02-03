controllore = True

while controllore:
    print("ciao")
    
    scelta = input("scegli esci per fermare il ciclo")
    
    if scelta == "esci":
        controllore= False
        

numeri = [1,2,3,4,5]

for pippo in numeri:
    print(pippo)
    
numeri2 = range(5)

for pippo in numeri2:
    print(pippo)
    
x= int(input())
    
for pippo in range(x):
    print(pippo)




pari_count = 0        
numeri_pari = []      

while pari_count < 5:
    numero = int(input("Inserisci un numero intero: "))

    # Controllo se il numero è pari
    if numero % 2 == 0:
        pari_count += 1
        numeri_pari.append(numero)
        print("Il numero è pari.")
    else:
        print("Il numero è dispari.")

# Quando ho inserito 5 numeri pari, esco dal ciclo
print("\nHai inserito 5 numeri pari.")
print("Questi numeri pari sono:", numeri_pari)
