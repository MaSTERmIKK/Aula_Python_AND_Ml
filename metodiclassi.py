class Pippo:
    aumento = 0
    
    def saluta():
        print("ciao Mirko")
        
    @classmethod
    def aumenta():
        Pippo.aumento += 1
        print(Pippo.aumento)
        
    @staticmethod
    def somma(a,b):
        return a + b
    
p = Pippo()

p.saluta()

p.aumenta()
Pippo.aumenta()

x = Pippo.somma(2,4)