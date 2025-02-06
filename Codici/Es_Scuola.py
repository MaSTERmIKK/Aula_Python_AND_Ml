
class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome
        self.__eta = eta

    # Getter e setter per nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    # Getter e setter per età
    def get_eta(self):
        return self.__eta

    def set_eta(self, eta):
        self.__eta = eta

    def presentazione(self):
        return f"Mi chiamo {self.__nome} e ho {self.__eta} anni."


class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)
        self.__voti = voti

    # Getter e setter per voti
    def get_voti(self):
        return self.__voti

    def set_voti(self, voti):
        self.__voti = voti

    def __calcola_media(self):
        return sum(self.__voti) / len(self.__voti) if self.__voti else 0

    def presentazione(self):  # Override senza polimorfismo
        return f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. La mia media voti è {self.__calcola_media():.2f}."


class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.__materia = materia

    # Getter e setter per materia
    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    def presentazione(self):  # Override senza polimorfismo
        return f"Mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. Insegno {self.__materia}."


# Test delle classi
studente = Studente("Luca", 20, [28, 30, 26, 29])
professore = Professore("Prof. Rossi", 45, "Matematica")

print(studente.presentazione())
print(professore.presentazione())
