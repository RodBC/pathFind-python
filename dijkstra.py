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
        self.lista_PESO = []

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
            print_origem = origem
            print_destino = destino

            origem = g.Locais.index(origem)
            destino = g.Locais.index(destino)


            tamanho_caminho, antecessores = g.dijkstra(origem, destino)
            caminho = []

            while destino != None:
                x = g.Locais[destino]
                caminho.append(x)
                destino = antecessores[destino]

            if tamanho_caminho != None:
                lista_final = []
                string_final = ""
                result = []

                for i in caminho[::-1]:
                    lista_final.append(i)
                    string_final +=i
                    string_final += "--> "

                string_final = string_final[:-4]
                result.append(f"Distância: {tamanho_caminho * 1.60934:.1f} Km  ")
                result.append(f" pelo caminho --{ string_final}")
                imprime = "".join(result)
                return("MENOR CAMINHO:", imprime)
            else:
                return(f"Não existe caminhos entre {print_origem} e {print_destino}")

g = Grafo()
graph = []
arquivo = open("Dados.txt", "r")

with arquivo:
    for line in arquivo:
        origem, dest, w = line.split()
        if origem not in g.Locais:
            g.Locais.append(origem)
        if dest not in g.Locais:
            g.Locais.append(dest)
        g.lista_PESO.append(w)
        graph.append([origem, dest])

arquivo2 = open("Dados.txt", "r")

with arquivo2:
    for line in arquivo2:
        origem, destino, peso = line.split()
        g.add_vertice(origem, destino, int(peso))

