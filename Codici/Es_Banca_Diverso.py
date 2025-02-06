from abc import ABC, abstractmethod

# Classe base astratta
class MetodoPagamento(ABC):
    @abstractmethod
    def effettua_pagamento(self, importo):
        pass

# Sottoclassi concrete
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Carta di Credito.")

class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato tramite PayPal.")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        print(f"Pagamento di {importo}€ effettuato con Bonifico Bancario.")

# Classe GestorePagamenti
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento
    
    def esegui_pagamento(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

# Esempio d'uso
def main():
    carta = CartaDiCredito()
    paypal = PayPal()
    bonifico = BonificoBancario()
    
    gestore1 = GestorePagamenti(carta)
    gestore2 = GestorePagamenti(paypal)
    gestore3 = GestorePagamenti(bonifico)
    
    gestore1.esegui_pagamento(100)
    gestore2.esegui_pagamento(200)
    gestore3.esegui_pagamento(300)

if __name__ == "__main__":
    main()
