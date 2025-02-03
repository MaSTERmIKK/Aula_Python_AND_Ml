# creiamo un sistema di if che ci permetta di riempire dei dati
# (Nome, età, cap, e un booleano di riferimento)  

nome = ""
eta = 0
cap = 0
boolRif = False

if nome == "" and eta == 0 and cap == 0 and boolRif == False:
    nome = input("iserisci il nome")
    if nome != "" and eta == 0 and cap == 0 and boolRif == False:
        eta = int(input("inserisci l'età"))
        if nome != "" and eta > 0  and cap == 0 and boolRif == False:
            cap = int(input("inserisci il tuo cap"))
            if nome != "" and eta > 0  and cap != 0 and boolRif == False:
                # boolRif = True
                
                riferimento = int(input("inserisci o 1 o 0"))
                if (riferimento > 0):
                    boolRif = False
                    print(nome, eta, cap, boolRif)
                elif(riferimento <= 0):
                    boolRif = True
                    print(nome, eta, cap, boolRif)
                else:
                    print("pippo hai sbagliato a digitare")
