class CartaDiCredito:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

class PayPal:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato tramite PayPal.")

class BonificoBancario:
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario.")

class GestorePagamenti:
    def __init__(self, metodo_pagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def esegui_pagamento(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

while True:
    metodo = input("Scegli un metodo di pagamento (carta, paypal, bonifico, esci): ").strip().lower()
    if metodo == "esci":
        break
    importo = float(input("Inserisci l'importo del pagamento: "))
    
    if metodo == "carta":
        gestore = GestorePagamenti(CartaDiCredito())
    elif metodo == "paypal":
        gestore = GestorePagamenti(PayPal())
    elif metodo == "bonifico":
        bonifico = BonificoBancario()
        gestore = GestorePagamenti(bonifico)    #è uguale a sopra
    else:
        print("Metodo non valido, riprova.")
        continue
    
    gestore.esegui_pagamento(importo)


