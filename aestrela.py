# -*- coding: utf8 -*-

# Este código implementa a busca A* para o exemplo da seção
# "3.5.2: A* search", do livro "Artificial Intelligence: A Modern
# Approach", 4ª edição, de Russell e Norvig (pág. 103-107). Neste
# exemplo utiliza-se o A* para encontrar o caminho ótimo entre as
# cidades de Arad e Bucareste (na verdade o algoritmo está preparado
# para encontrar o caminho ótimo entre as 19 cidades Romenas consideradas
# no algoritmo como pontos de início, e a cidade de Bucareste considerada
# como destino). Bucareste deve ser considerada o destino neste exemplo
# pois a função heurística h(n) informa as distâncias em linha reta entre
# as demais cidades e a cidade de Bucareste.
#
# Alunos: Abrantes, João Benincá, Jordhan, Luan, Renata, Vinícius

# Dicionário que implementa uma lista de adjacências para o grafo
# não-direcionado entre diversas cidades Romenas. Essas informações
# foram retiradas da Figura 3.1 do livro de referência citado acima.
# Essas distâncias representam a função de custo g(n) para, de um nó,
# se chegar a outro nó conexo.
dic_adj = {
    'ORADEA':    [('ZERIND', 71),     ('SIBIU', 151)],
    'ZERIND':    [('ORADEA', 71),     ('ARAD', 75)],
    'ARAD':      [('ZERIND', 75),     ('TIMISOARA', 118),  ('SIBIU', 140)],
    'TIMISOARA': [('ARAD', 118),      ('LUGOJ', 111)],
    'LUGOJ':     [('TIMISOARA', 111), ('MEHADIA', 70)],
    'MEHADIA':   [('LUGOJ', 70),      ('DROBETA', 75)],
    'DROBETA':   [('MEHADIA', 75),    ('CRAIOVA', 120)],
    'SIBIU':     [('ORADEA', 151),    ('ARAD', 140),       ('RIMNICU', 80),     ('FAGARAS', 99)],
    'RIMNICU':   [('SIBIU', 80),      ('CRAIOVA', 146),    ('PITESTI', 97)],
    'CRAIOVA':   [('DROBETA', 120),   ('RIMNICU', 146),    ('PITESTI', 138)],
    'FAGARAS':   [('SIBIU', 99),      ('BUCARESTE', 211)],
    'PITESTI':   [('RIMNICU', 97),    ('CRAIOVA', 138),    ('BUCARESTE', 101)],
    'BUCARESTE': [('FAGARAS', 211),   ('PITESTI', 101),    ('GIURGIU', 90),     ('URZICENI', 85)],
    'GIURGIU':   [('BUCARESTE', 90)],
    'NEAMT':     [('IASI', 87)],
    'IASI':      [('NEAMT', 87),      ('VASLUI', 92)],
    'VASLUI':    [('IASI', 92),       ('URZICENI', 142)],
    'URZICENI':  [('BUCARESTE', 85),  ('VASLUI', 142),     ('HIRSOVA', 98)],
    'HIRSOVA':   [('URZICENI', 98),   ('EFORIE', 86)],
    'EFORIE':    [('HIRSOVA', 86)]
}


# Função heurística h(n) que retorna a distância em linha reta entre
# qualquer cidade e a cidade de Bucareste. Retiramos essas informações
# da Figura 3.16 do livro de referência citado acima.
def heuristica(n):
    h = {
        'ARAD': 366,
        'BUCARESTE': 0,
        'CRAIOVA': 160,
        'DROBETA': 242,
        'EFORIE': 161,
        'FAGARAS': 176,
        'GIURGIU': 77,
        'HIRSOVA': 151,
        'IASI': 226,
        'LUGOJ': 244,
        'MEHADIA': 241,
        'NEAMT': 234,
        'ORADEA': 380,
        'PITESTI': 100,
        'RIMNICU': 193,
        'SIBIU': 253,
        'TIMISOARA': 329,
        'URZICENI': 80,
        'VASLUI': 199,
        'ZERIND': 374
    }
    return h[n]


# Cria a classe Grafo, que recebe o dicionário com a lista de adjacências
class Grafo:
    def __init__(self, p_mat_adj):
        self.mat_adj = p_mat_adj

    def get_vizinhos(self, v):
        return self.mat_adj[v]

    def a_estrela(self, inicio, destino):
        # A lista_aberta é a lista de nós que já foram visitados mas cujos
        # vizinhos (nós conexos) ainda não foram todos inspecionados. Essa
        # lista é iniciada com o nó "inicio" (a cidade de origem).
        lista_aberta = set([inicio])

        # A lista_fechada é a lista de nós que já foram visitados e cujos
        # vizinhos também já foram inspecionados.
        lista_fechada = set([])

        # Mantém as distâncias do nó a todos os outros nós.
        dist = {inicio: 0}

        # Mantém um mapeamento de todos os outros nós adjacentes.
        mapadj = {inicio: inicio}

        # A busca A* continua enquanto a lista_aberta não for vazia
        while len(lista_aberta) > 0:
            n = None

            # Verifica a lista_aberta e encontra o nó com o menor valor
            # de custo, o menor valor de f(n) dado por f(n) = g(h) + h(n)
            for v in lista_aberta:
                if n is None or (dist[v] + heuristica(v) < dist[n] + heuristica(n)):
                    n = v

            # Se não há nenhum nó na list_aberta que tenha o menor custo,
            # então não há caminho. Mostra mensagem e sai.
            if n is None:
                print('Não existe caminho para o destino!')
                return None

            # Se o nó atual é o nó de destino (Bucareste), então
            # constrói o caminho até o nó.
            if n == destino:
                determina_path = []

                while mapadj[n] != n:
                    determina_path.append(n)
                    n = mapadj[n]

                determina_path.append(inicio)

                determina_path.reverse()

                print('Caminho encontrado: {}'.format(determina_path))
                return determina_path

            # Para todos os vizinhos do nó atual:
            for (cidade, milhas) in self.get_vizinhos(n):
                # Se a cidade não está na lista_aberta e também não está
                # na lista fechada, então ele é adicionado na lista_aberta
                # e o vizinho n é alocado no mapa de cidades vizinhas
                if (cidade not in lista_aberta) and (cidade not in lista_fechada):
                    lista_aberta.add(cidade)
                    mapadj[cidade] = n
                    dist[cidade] = dist[n] + milhas
                # Caso contrário, verificamos se é mais rápido visitar n
                # e depois a cidade e, se for, atualizamos o mapa de adjacências
                # e as distâncias, e se o nó está na lista_fechada, é
                # recolocado na lista_aberta
                else:
                    if dist[cidade] > dist[n] + milhas:
                        dist[cidade] = dist[n] + milhas
                        mapadj[cidade] = n

                        if cidade in lista_fechada:
                            lista_fechada.remove(cidade)
                            lista_aberta.add(cidade)

            # Remove n da lista_aberta e coloca na lista_fechada, após
            # inspecionar todos os seus vizinhos.
            lista_aberta.remove(n)
            lista_fechada.add(n)

        # Se chegamos até aqui, verificamos tudo e não achamos um
        # caminho.
        print('Caminho não existe')
        return None


grafo1 = Grafo(dic_adj)
grafo1.a_estrela('TIMISOARA', 'BUCARESTE')
