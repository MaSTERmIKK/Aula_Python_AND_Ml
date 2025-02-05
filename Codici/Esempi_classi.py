# Definizione di una classe base chiamata Punto
class Punto:
    # Il costruttore __init__ viene utilizzato per inizializzare gli attributi della classe
    def __init__(self, x, y):
        self.x = x  # Attributo x del punto
        self.y = y  # Attributo y del punto

    # Metodo per spostare il punto in una nuova posizione
    def sposta(self, nuovo_x, nuovo_y):
        self.x = nuovo_x
        self.y = nuovo_y

    # Metodo per ottenere una rappresentazione stringa del punto
    def __str__(self):
        return f"fedrica: ({self.x}, {self.y}, {self.voto})"

# Utilizzo della classe Punto
p = Punto(2, 3)
print(p)  # Output: Punto(2, 3)
p.sposta(5, 7)
print(p)  # Output: Punto(5, 7)

lista = [p]
print(lista[0])




# Definizione di una classe base chiamata Rettangolo
class Rettangolo:
    # Il costruttore __init__ per inizializzare larghezza e altezza
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza


    def modifica(self, nuovo_larghezza, nuovo_altezza):
        self.larghezza = nuovo_larghezza
        self.altezza = nuovo_altezza

    # Metodo per calcolare l'area del rettangolo
    def area(self):
        return self.larghezza * self.altezza

    # Metodo per calcolare il perimetro del rettangolo
    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)

    # Metodo per ottenere una rappresentazione stringa del rettangolo
    def __str__(self):
        return f"Rettangolo({self.larghezza}, {self.altezza})"

# Utilizzo della classe Rettangolo
r = Rettangolo(4, 5)
print(r)  # Output: Rettangolo(4, 5)
print("Area:", r.area())  # Output: Area: 20
print("Perimetro:", r.perimetro())  # Output: Perimetro: 18
r.modifica(10, 15)
print("Area:", r.area())  # Output: Area: ??
print("Perimetro:", r.perimetro())  # Output: Perimetro: ??


# Definizione di una classe base chiamata Cerchio
class Cerchio:
    # Importiamo il modulo math per calcoli matematici
    import math
    
    # Il costruttore __init__ per inizializzare il raggio
    def __init__(self, raggio):
        self.raggio = raggio

    # Metodo per calcolare l'area del cerchio
    def area(self):
        return self.math.pi * (self.raggio ** 2)

    # Metodo per calcolare la circonferenza del cerchio
    def circonferenza(self):
        return 2 * self.math.pi * self.raggio

    # Metodo per ottenere una rappresentazione stringa del cerchio
    def __str__(self):
        return f"Cerchio({self.raggio})"

# Utilizzo della classe Cerchio
c = Cerchio(3)
print(c)  # Output: Cerchio(3)
print("Area:", c.area())  # Output: Area: 28.274333882308138
print("Circonferenza:", c.circonferenza())  # Output: Circonferenza: 18.84955592153876



# Definizione di una classe base chiamata Studente
class Studente:
    # Il costruttore __init__ per inizializzare nome e voti
    def __init__(self, nome, voti):
        self.nome = nome
        self.voti = voti

    # Metodo per calcolare la media dei voti dello studente
    def media_voti(self):
        return sum(self.voti) / len(self.voti)

    # Metodo per ottenere una rappresentazione stringa dello studente
    def __str__(self):
        return f"Studente({self.nome}, Media voti: {self.media_voti()})"

# Utilizzo della classe Studente
s = Studente("Mario Rossi", [28, 30, 26, 24])
print(s)  # Output: Studente(Mario Rossi, Media voti: 27.0)



# Definizione di una classe base chiamata Libro
class Libro:
    # Il costruttore __init__ per inizializzare il titolo, l'autore e il numero di pagine
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # Metodo per ottenere una rappresentazione stringa del libro
    def __str__(self):
        return f"Libro('{self.titolo}', di {self.autore}, {self.pagine} pagine)"

# Utilizzo della classe Libro
l = Libro("Il nome della rosa", "Umberto Eco", 500)
print(l)  # Output: Libro('Il nome della rosa', di Umberto Eco, 500 pagine)





# Definizione di una classe base chiamata ContoBancario
class ContoBancario:
    # Il costruttore __init__ per inizializzare il saldo del conto
    def __init__(self, saldo_iniziale):
        self.saldo = saldo_iniziale

    # Metodo per depositare una somma di denaro nel conto
    def deposita(self, somma):
        self.saldo += somma

    # Metodo per prelevare una somma di denaro dal conto
    def preleva(self, somma):
        if somma <= self.saldo:
            self.saldo -= somma
        else:
            print("Saldo insufficiente")

    # Metodo per ottenere una rappresentazione stringa del conto bancario
    def __str__(self):
        return f"ContoBancario(saldo: {self.saldo}€)"

# Utilizzo della classe ContoBancario
c = ContoBancario(1000)
print(c)  # Output: ContoBancario(saldo: 1000€)
c.deposita(500)
print(c)  # Output: ContoBancario(saldo: 1500€)
c.preleva(300)
print(c)  # Output: ContoBancario(saldo: 1200€)
c.preleva(1500)  # Output: Saldo insufficiente
print(c)  # Output: ContoBancario(saldo: 1200€)



# Definizione di una classe base chiamata Automobile
class Automobile:
    # Il costruttore __init__ per inizializzare il modello, il colore e la velocità
    def __init__(self, modello, colore, velocita_massima):
        self.modello = modello
        self.colore = colore
        self.velocita_massima = velocita_massima
        self.velocita_attuale = 0

    # Metodo per accelerare l'automobile
    def accelera(self, incremento):
        nuova_velocita = self.velocita_attuale + incremento
        if nuova_velocita > self.velocita_massima:
            self.velocita_attuale = self.velocita_massima
        else:
            self.velocita_attuale = nuova_velocita

    # Metodo per frenare l'automobile
    def frena(self, decremento):
        nuova_velocita = self.velocita_attuale - decremento
        if nuova_velocita < 0:
            self.velocita_attuale = 0
        else:
            self.velocita_attuale = nuova_velocita

    # Metodo per ottenere una rappresentazione stringa dell'automobile
    def __str__(self):
        return f"Automobile({self.modello}, {self.colore}, Velocità attuale: {self.velocita_attuale} km/h)"

# Utilizzo della classe Automobile
a = Automobile("Fiat 500", "Rosso", 180)
print(a)  # Output: Automobile(Fiat 500, Rosso, Velocità attuale: 0 km/h)
a.accelera(50)
print(a)  # Output: Automobile(Fiat 500, Rosso, Velocità attuale: 50 km/h)
a.accelera(150)
print(a)  # Output: Automobile(Fiat 500, Rosso, Velocità attuale: 180 km/h)
a.frena(60)
print(a)  # Output: Automobile(Fiat 500, Rosso, Velocità attuale: 120 km/h)
