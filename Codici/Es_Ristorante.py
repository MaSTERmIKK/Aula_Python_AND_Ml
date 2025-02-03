class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  # Il ristorante è chiuso di default
        self.menu_piatti = []  # Lista dei nomi dei piatti
        self.menu_prezzi = []  # Lista dei prezzi corrispondenti ai piatti

    def descrivi_ristorante(self):
        print(f"Il ristorante '{self.nome}' offre cucina {self.tipo_cucina}.")
    
    def stato_apertura(self):
        print("Il ristorante è aperto." if self.aperto else "Il ristorante è chiuso.")
    
    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è ora aperto.")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante è ora chiuso.")
    
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu_piatti.append(piatto)
        self.menu_prezzi.append(prezzo)
        print(f"Aggiunto {piatto} al menu con prezzo {prezzo:.2f}€.")
    
    def togli_dal_menu(self, piatto):
        if piatto in self.menu_piatti:
            indice = self.menu_piatti.index(piatto)
            self.menu_piatti.pop(indice)
            self.menu_prezzi.pop(indice)
            print(f"Rimosso {piatto} dal menu.")
        else:
            print(f"{piatto} non è presente nel menu.")
    
    def stampa_menu(self):
        print("Menu del ristorante:")
        for piatto, prezzo in zip(self.menu_piatti, self.menu_prezzi):
            print(f"- {piatto}: {prezzo:.2f}€")

# Test della classe
ristorante = Ristorante("La Buona Tavola", "Italiana")
ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.aggiungi_al_menu("Pasta Carbonara", 12.50)
ristorante.aggiungi_al_menu("Pizza Margherita", 8.00)
ristorante.stampa_menu()
ristorante.togli_dal_menu("Pasta Carbonara")
ristorante.stampa_menu()
ristorante.chiudi_ristorante()
