# Classe base che rappresenta un prodotto generico
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        # Inizializza gli attributi comuni a tutti i prodotti
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        # Ritorna la differenza tra il prezzo di vendita e il costo di produzione
        return self.prezzo_vendita - self.costo_produzione


# Classe per prodotti di tipo Elettronica, che usa la composizione con Prodotto
class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        # Crea un'istanza di Prodotto per gestire gli attributi comuni
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

    def calcola_profitto(self):
        # Utilizza il metodo della classe Prodotto
        return self.prodotto.calcola_profitto()

    def get_nome(self):
        # Restituisce il nome del prodotto
        return self.prodotto.nome


# Classe per prodotti di tipo Abbigliamento, che usa la composizione con Prodotto
class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        # Crea un'istanza di Prodotto per gestire gli attributi comuni
        self.prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

    def calcola_profitto(self):
        # Utilizza il metodo della classe Prodotto
        return self.prodotto.calcola_profitto()

    def get_nome(self):
        # Restituisce il nome del prodotto
        return self.prodotto.nome


# Classe Fabbrica che gestisce l'inventario e le operazioni di vendita/reso
class Fabbrica:
    def __init__(self):
        # L'inventario è un dizionario: chiave = nome del prodotto, valore = dizionario con il prodotto e la quantità
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita=1):
        # Recupera il nome del prodotto tramite il metodo get_nome (definito nelle classi specifiche)
        nome_prodotto = prodotto.get_nome()
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
        else:
            self.inventario[nome_prodotto] = {'prodotto': prodotto, 'quantita': quantita}
        print("Aggiunte " + str(quantita) + " unità di " + nome_prodotto + " all'inventario.")

    def vendi_prodotto(self, nome_prodotto, quantita=1):
        if nome_prodotto in self.inventario:
            record = self.inventario[nome_prodotto]
            if record['quantita'] >= quantita:
                record['quantita'] -= quantita
                profitto = quantita * record['prodotto'].calcola_profitto()
                print("Vendute " + str(quantita) + " unità di " + nome_prodotto + ". Profitto realizzato: " + str(profitto))
            else:
                print("Inventario insufficiente per vendere " + str(quantita) + " unità di " + nome_prodotto + ". Quantità disponibili: " + str(record['quantita']))
        else:
            print("Prodotto " + nome_prodotto + " non trovato in inventario.")

    def resi_prodotto(self, nome_prodotto, quantita=1):
        if nome_prodotto in self.inventario:
            self.inventario[nome_prodotto]['quantita'] += quantita
            print("Resi " + str(quantita) + " unità di " + nome_prodotto + ".")
        else:
            print("Prodotto " + nome_prodotto + " non trovato in inventario. Impossibile processare il reso.")
