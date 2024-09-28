class carro:
    def __init__(self,marca,modelo,cor,combustivel) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0
   
   
    def ligar(self):
        if self.ligado:
            print("Carro ja esta ligado")
        else:
            print("carro,ligado")
            self.ligado = True



    def desligado(self):                      
        if self.ligado:
         print("carro,desligado")
    
        else: 
            print("carro desligado")
            self.ligado = False

    def acelerar(self):
        if self.ligado:
            self.velocidade += 1
            print(f"{self.velocidade}Km/h")
        else:
           print("Nao e possivel acelerar, carro desligado")     
