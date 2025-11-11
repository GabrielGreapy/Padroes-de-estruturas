O Adapter é um modelo estrutural que busca tornar a comunicação entre tipos diferente de interfaces
tornando elas conversaveis entre si quando sem o Adaptador não seria possivel, por isso precisamos de uma classe adaptadora.
Quando alguem vai até um país estrangeiro e precisamos de um tradutor para traduzir informações de residentes.
o tradutor seria o adaptador que te passa a informação de uma forma que você entenda.
Dando um exemplo simples.
vamos dizer que temos uma situação em que um segurança precisa saber seu nome numa festa e você está
com uma dor de garganta, você decide escrever no seu braço mas o segurança é analfabeto, aqui precisamos de alguem para ler e 
dizer ao segurança para você
Classes:
    Segurança(Target) : precisa de uma string (seu nome), não consegue ler o nome escrito
    Você(Adaptee) : precisa passar o seu nome mas não pode falar diretamente ao segurança
    Tradutor(Adapter) : Pode entender você e pode passar a info pro segurança.

    Target seria o alvo que precisa dos dados adaptados.
    Adaptee seria o que entrega os dados que precisam ser adaptados.
    Adapter seria aquele que traduz, adapta e entre ao Target.
