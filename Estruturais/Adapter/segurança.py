class seguranca_target:
    def request(self) -> str:
        return("O segurança precisa desse dado em especifico.")
    
class voce_adaptee:
    def specific_request(self) -> str:
        return "leirbaG"
    

class tradutor_adapter:
    def __init__(self, adaptee : "voce_adaptee"):
        self._adaptee = adaptee
    def request(self) -> str:
        dado_invertido = self._adaptee.specific_request()
        dado_traduzido = dado_invertido[::-1]
        return f"Tradutor(Adapter): (Traduzido) {dado_traduzido}"

    
    

def seguranca_alfabetizado(seguranca_target : "seguranca_target") -> None:
    print(f"{seguranca_target.request()}", end="  ")


if __name__ == "__main__":
    print("Opa, nesse universo um temos segurança alfabetizado, é um universo que focaram" \
    "na educação e foi efetivo.")
    target = seguranca_target()
    seguranca_alfabetizado(target)
    adaptee = voce_adaptee()
    print("Mas aqui estamos na realidade(imaginada), o segurança não consegue ler o que está escrito no meu braço. \n agora precisamos" \
    "de um tradutor mas veja como não consigo")
    print(f"Adaptee : {adaptee.specific_request()}", end ="  ")
    print("Adaptee: mas eu consigo se alguem ler pra mim")
    adapter = tradutor_adapter(adaptee)
    adapter.request()
    seguranca_alfabetizado(adapter)

