# Matriz visual usada pra montar a matriz de adjacência
matriz = [ [0, 1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12, 13],
           [14, 15, 16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25, 26, 27],
           [28, 29, 30, 31, 32, 33, 34],
           [35, 36, 37, 38, 39, 40, 41],
           [42, 43, 44, 45, 46, 47, 48],
        ]
'''
0    1     |2   3|  4   5  6
    ---
7    8     |9  10  11  12 |13
----               ------
14   15    16 |17 18  19  20
      ------              ---
21   22   23  |24 25 |26  27
---           ------     ---
28   29  |30 |31  32 |33  34
     ---
35   36  37  38  39  40  41
          ------          ---
42  |43  44  |45  46 |47  48
'''

# nos é uma matriz onde suas chaves representam a posíção no labirinto
# E seu valor representa os possíveis lugares que voce pode andar
# sempre iniciará do 0 para alterar será nes
nos = [
    [1,7],#nó 0
    [0],#nó 1
    [3, 9],#nó 2
    [2, 10],#nó 3
    [5, 11],#nó 4
    [4, 6, 12],#nó 5
    [5, 13],#nó 6
    [0, 8],#nó 7
    [7, 15], #nó 8
    [2, 10, 16], #nó 9
    [3, 9, 11, 17], #nó 10
    [4, 10, 12], #nó 11
    [5, 11], #nó 12
    [6, 20], #nó 13
    [15, 21], #nó 14
    [8, 14, 16], #nó 15
    [9, 15], #nó 16
    [10, 18, 24], #nó 17
    [17, 19, 25], #nó 18
    [18, 20, 26], #nó 19
    [13, 19], #nó 20
    [14, 22], #nó 21
    [21, 23, 29], #nó 22
    [22, 30], #nó 23
    [17, 25], #nó 24
    [18, 24], #nó 25
    [19, 27, 33], #nó 26
    [26], #nó 27
    [29, 35], #nó 28
    [22, 28], #nó 29
    [23, 37], #nó 30
    [32, 38], #nó 31
    [31, 39], #nó 32
    [26, 34, 40], #nó 33
    [33, 41], #nó 34
    [28, 36, 42], #nó 35
    [35, 37, 43], #nó 36
    [30, 36, 38], #nó 37
    [31, 37, 39], #nó 38
    [32, 38, 40, 46], #nó 39
    [33, 39, 41, 47], #nó 40
    [34, 40], #nó 41
    [35], #nó 42
    [36, 44], #nó 43
    [43], #nó 44
    [46], #nó 45
    [39, 45], #nó 46
    [40, 48], #nó 47
    [47], #nó 48
]

class Grafo:
    def __init__(self, destino, node):
            self.destino = destino
            self.node = node

    def caminhar(self, pos, visitados, distancia):
        caminhos = self.node[pos]
        destino = self.destino
        distancias = []
        visitados.add(pos)
        if pos == destino:
            return distancia
        distancia += 1
        for novo_pos in caminhos:
            if novo_pos == destino:
                return distancia
            if not novo_pos in visitados:
                try:
                    distancias.append( self.caminhar(novo_pos,set(visitados), distancia) )
                except:
                    pass
        return min(distancias)

    def h(self, n):
        try:
            return self.caminhar(n,set(), 0)
        except:
            return None
    

class Caminho:
    def __init__(self, destino, node, grafo):
        self.destino = destino 
        self.node = node
        self.grafo = grafo

    def verificarCaminho(self, pos, g_anterior):
            valor = self.grafo.h(pos)
            if not valor:
                raise Exception('Não existe caminho para o destino escolhido')
            return g_anterior + valor
    
    def getCaminho(self, n):
        pos = n
        g = 0
        path = [pos]
        try:
            while True:
                menor = 999999
                indexMenor = -1
                caminhos = self.node[pos]
                for caminho in caminhos:
                    if caminho == self.destino:
                        path.append(caminho)
                        return path
                    if caminho in path:
                        continue
                    heuristica = self.verificarCaminho(caminho, g+1)
                    if heuristica < menor:
                        menor = heuristica
                        indexMenor = caminho
                if indexMenor != -1:
                    pos = indexMenor
                    path.append(indexMenor)
                    g += 1
                    continue
                else:
                    break
        except:
            return []
        return path

#Função para testar qual a distância espacial do nó 0 para o nó final capturado pelo argumento
#caso não passe ele setará o 8
final = 48
grafo = Grafo(final, nos)

#Calcula o caminho do inicio ao fim
calcularCaminho = Caminho(final, nos, grafo)

#Pega o resultado e faz o desenho do caminho percorrido no labirinto
caminhoFinal = ''
caminhos = calcularCaminho.getCaminho(0)
for i in range( len(caminhos) ):
    passagem = caminhos[i]
    if i != 0:
        caminhoFinal += ' -> '
    caminhoFinal += str(passagem)

print(caminhoFinal)