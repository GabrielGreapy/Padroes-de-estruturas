O objetivo do FlyWeight é economizar memoria RAM.

Quando em um projeto há muitos objetos identicos (Exemplo: um jogo com folhas flutuando ao vento) , O jogo ocuparia muito espaço na
CPU que na verdade não é necessario,
Pois muitas folhas identicas estão sendo renderizada. 
Vamos dizer que as variaveis das folhas são o seguinte:
    textura : folha.png,
    movimento : folhaAoVento(),
    coordenadaX: X,
    coordenadaY : Y,

Com dezenas de folhas ao vento voando o computador começaria a ficar cheio demais podendo até fechar o programa qe está rodando.
Só imaginar dezenas de "folha.png" sendo criadas e sumindo, atrapalharia muito.

Com isso o flyweight vem com uma solução simples: Separar as variaveis de cada folha em dois tipos de dados diferentes
Estados Intrisicos e Estados Extrinsicos.

estado intrisicos seria aqueles dados que se repetem entre todas as folhas, no caso seria o folha.png e o movimento que seria
uma função chamada folhaAoVento. Esse dado não precisa ter exatamente em todo objeto, só precisamos de uma folha.png que se repete entre todos.
    Estados intrisico (  Que repete entre todas folhas):
    textura : folha.png,
    movimento : folhaAoVento(),

estado extrinsicos seriam aqueles dados que são especiais e especificos para cada folha, como o lugar exato da tela em que ela está coordenadaX, coordenadaY.
    Estadis extrinsicos ( Que é especifico para cada folha)
    coordenadaX: X,
    coordenadaY : Y,

com isso na criação de cada folha só seria necessaria guardar os dados de coordenadas, poupando muito mais o espaço de RAM.