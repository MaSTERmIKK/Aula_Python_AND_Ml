# Esempio 1: Creazione e stampa di un dizionario
persona = {
    "nome": "Mario",
    "eta": 30,
    "citta": "Roma"
}
print("Dizionario persona:", persona)

# Esempio 2: Accesso agli elementi di un dizionario
print("Nome:", persona["nome"])
print("Età:", persona["eta"])
print("Città:", persona["citta"])

# Esempio 3: Aggiunta e aggiornamento di chiavi in un dizionario
persona["eta"] = 31                   # Aggiorna il valore di una chiave esistente
persona["professione"] = "Medico"     # Aggiunge una nuova chiave
print("\nDopo aggiornamento e aggiunta di chiavi:", persona)

# Esempio 4: Rimozione di chiavi da un dizionario
del persona["professione"]
print("Dopo rimozione della chiave 'professione':", persona)

# Esempio 5: Controllare l’esistenza di una chiave e usare una condizione
if "nome" in persona:
    print("\nLa chiave 'nome' esiste e il valore è:", persona["nome"])
else:
    print("\nLa chiave 'nome' non esiste nel dizionario.")

# Esempio 6: Iterare su un dizionario (chiavi e valori)
print("\nIterazione sul dizionario persona:")
for chiave, valore in persona.items():
    print("Chiave:", chiave, "| Valore:", valore)

# Esempio 7: Funzione che accetta un dizionario come parametro
def stampa_dettagli(diz):
    """
    Stampa chiave e valore di un dizionario in modo formattato.
    """
    print("\nDettagli del dizionario:")
    for k, v in diz.items():
        print(f" - {k}: {v}")

# Chiamata della funzione con il dizionario 'persona'
stampa_dettagli(persona)

# Esempio 8: Dizionario con liste come valori
agenda = {
    "mattina": ["Colazione", "Sport"],
    "pomeriggio": ["Lavoro", "Pranzo"],
    "sera": ["Cena", "Lettura"]
}
print("\nAgenda completa:", agenda)

# Iterare su un dizionario che contiene liste
for fascia_oraria, attivita in agenda.items():
    print(f"\nNella fascia '{fascia_oraria}' ho le seguenti attività:")
    for azione in attivita:
        print("  -", azione)  # qui va usato il emtodo se c'è un oggetto

# Esempio 9: Dizionario di dizionari
rubrica = {
    "contatto1": {
        "nome": "Luigi",
        "numero": "123456789"
    },
    "contatto2": {
        "nome": "Anna",
        "numero": "987654321"
    }
}

# Iterazione su un dizionario di dizionari
print("\nRubrica completa:")
for identificatore, info_contatto in rubrica.items():
    print(f"\nIdentificatore: {identificatore}")
    for chiave, valore in info_contatto.items():
        print(f"  {chiave.capitalize()}: {valore}")

# Esempio 10: Uso di una condizione con i valori di un dizionario
def verifica_numero(rubrica, contatto):
    """
    Verifica se esiste un contatto e se il numero telefonico inizia con '123'.
    """
    if contatto in rubrica:
        numero = rubrica[contatto]["numero"]
        if numero.startswith("123"):
            print(f"\nIl contatto '{contatto}' ha un numero che inizia con 123.")
        else:
            print(f"\nIl contatto '{contatto}' non ha un numero che inizia con 123.")
    else:
        print(f"\nIl contatto '{contatto}' non esiste nella rubrica.")

# Chiamata della funzione di verifica
verifica_numero(rubrica, "contatto1")
verifica_numero(rubrica, "contatto2")
verifica_numero(rubrica, "contatto3")  # contatto non esistente



# stamapre da oggetti

class Libro:
    titolo= "fear of the dark"
    def descrivi(self):
        print(self.titolo)
        

libro1 = Libro()
libro2 = Libro()

rubrica_libri = {}

rubrica_libri["libro1"] = libro1
rubrica_libri["libro2"] = libro2

for valore in rubrica_libri.values():
    valore.descrivi()
