from collections import defaultdict

class MinHeap:
    def __init__(self):
        self.nos = 0
        self.heap = []

    def insert(self, peso, indice):
        self.heap.append([peso, indice])
        self.nos += 1
        var = self.nos
        while True:
            if var == 1:
                break
            value = var // 2
            if self.heap[value - 1][0] <= self.heap[var - 1][0]:
                break
            else:
                self.heap[value - 1], self.heap[var - 1] = self.heap[var - 1], self.heap[value - 1]
                var = value

    def remove(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        p = 1
        while True:
            f = 2 * p
            if f > self.nos:
                break
            if f + 1 <= self.nos:
                if self.heap[f][0] < self.heap[f - 1][0]:
                    f += 1
            if self.heap[p - 1][0] <= self.heap[f - 1][0]:
                break
            else:
                self.heap[p - 1], self.heap[f - 1] = self.heap[f - 1], self.heap[p - 1]
                p = f
        return x

    def tamanho(self):
        return self.nos

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
        self.Locais = []

    def add_vertice(self, origem, destino, peso):
        valor_origem = self.Locais.index(origem)
        valor_destino = self.Locais.index(destino)
        self.grafo[valor_origem].append((valor_destino, peso))


    def dijkstra(self, origem, destino):
        tamanho = len(g.Locais)
        peso = [None] * tamanho
        antecessor = [None] * tamanho

        peso[origem] = 0

        min_heap = MinHeap()
        min_heap.insert(0, origem)

        while min_heap.tamanho() > 0:
            weight, vert = min_heap.remove()

            for aresta in self.grafo[vert]:
                v, custo = aresta

                if peso[v] is None or peso[v] > peso[vert] + custo:
                    peso[v] = peso[vert] + custo
                    antecessor[v] = vert

                    min_heap.insert(peso[v], v)
        return peso[destino], antecessor

    def calcula_caminho(self, origem, destino):
        if origem not in g.Locais or destino not in g.Locais:
            return False
        else:
            print_origem = origem
            print_destino = destino
            origem = g.Locais.index(origem)
            destino = g.Locais.index(destino)
            caminho = []
            tamanho_caminho, antecessores = g.dijkstra(origem, destino)

            while destino != None:
                x = g.Locais[destino]
                caminho.append(x)
                destino = antecessores[destino]
            if tamanho_caminho != None:
                lista_final = []
                for i in caminho[::-1]:
                    lista_final.append(i)
                    lista_final.append("-->")
                lista_final.pop(-1)
                return (f"O menor caminho custa: {tamanho_caminho} km ||  "
                       f"O menor caminho é: {lista_final}")
            else:
                return (f"Não existe caminhos entre {print_origem} e {print_destino}")

g = Grafo()


'''Salva todos os locais em uma lista'''

arquivo = open("Dados.txt", "r")

with arquivo:
    for line in arquivo:
        origem, distancia, w = line.split()
        if origem not in g.Locais:
            g.Locais.append(origem)
        if distancia not in g.Locais:
            g.Locais.append(distancia)


'''adiciona vertices e seus pesos no grafo'''

arquivo2 = open("Dados.txt", "r")

with arquivo2:
    for line in arquivo2:
        origem, destino, peso = line.split()
        g.add_vertice(origem, destino, int(peso))


print(f"lista de aeroportos: {g.Locais}")


'''Imprime o output'''

def getRoute(origem, destino, Bool=False):
    while Bool != True:
        Resultado = g.calcula_caminho(origem, destino)

        if Resultado == False:
            return("Esse Aeroporto não existe na nossa base dados! Tente outro local.")
        else:
            Bool = True
            return(Resultado)
