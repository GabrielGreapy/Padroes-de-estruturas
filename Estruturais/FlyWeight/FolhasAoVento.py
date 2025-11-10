class tipoDeFolha:
    def __init__(self, textura, movimento):
        print(f"Carregando folha : {textura} e {movimento}")
        self.textura = textura
        self.movimento = movimento
    def renderizandoFolha(self, x, y):
        print(f"Desenhando '{self.textura}' em (X={x}, Y={y}) com movimento '{self.movimento}'")

class Folha:
    def __init__(self, x, y, tipoDeFolha):
        self.x = x 
        self.y = y
        self.tipoDeFolha = tipoDeFolha
    def renderizar(self):
        self.tipoDeFolha.renderizandoFolha( self.x , self.y)
        print(f"Renderizando folha em coordenadas {self.x} e {self.y}, sendo o tipo de folha {self.tipoDeFolha}.")


class FabricaDeFolhas:
    def __init__(self):
        self._tiposDeFolhas = {}
    def getTipoDeFolhas(self, textura, movimento):
        chave = (textura, movimento)
        if chave not in self._tiposDeFolhas:
            print("Fábrica: Não achei esse tipo. Vou criar um novo...")
            self._tiposDeFolhas[chave] = tipoDeFolha(textura, movimento)
        else: print("Fabrica: Já temos uma dessas, Reutilizando...")
        return self._tiposDeFolhas[chave]





import random


folhas_na_tela = []


fabrica = FabricaDeFolhas()

print("### Criando 5 folhas 'folha_outono.png' ###")

tipo_outono = fabrica.getTipoDeFolhas("folha_outono.png", "folhaAoVento_rapido")


for _ in range(5):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    folhas_na_tela.append(Folha(x, y, tipo_outono))

print("\n### Criando 5 folhas 'folha_verde.png' ###")

tipo_verde = fabrica.getTipoDeFolhas("folha_verde.png", "folhaAoVento_lento")


for _ in range(5):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    folhas_na_tela.append(Folha(x, y, tipo_verde))

print("\n--- O Jogo está rodando, desenhando todas as folhas ---")

for folha in folhas_na_tela:
    folha.renderizar()


print("\n===============================")
print(f"Total de folhas 'leves' na tela (Contextos): {len(folhas_na_tela)}")
print(f"Total de tipos 'pesados' em memória (Flyweights): {len(fabrica._tiposDeFolhas)}")