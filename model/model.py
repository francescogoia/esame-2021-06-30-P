import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def crea_grafo(self):
        self._nodes = DAO.getAllNodes()
        self._grafo.add_nodes_from(self._nodes)
        archi = DAO.getAllEdges()
        for a in archi:
            u = a[0]
            v = a[1]
            peso = a[2]
            self._grafo.add_edge(u, v, weight=peso)

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getnNeighboors(self, localizzazione):
        result = []
        vicini = self._grafo.neighbors(localizzazione)
        for v in vicini:
            result.append((v, self._grafo[localizzazione][v]["weight"]))
        return result

    def handlePath(self, loc):
        self._bestPath = []
        self._bestSol = 0
        self._ricorsione(loc, [])

        return self._bestPath, self._bestSol

    def _ricorsione(self, partenza, parziale):
        peso_parziale = self.calocaPesoParziale(parziale)
        if peso_parziale > self._bestSol:
            self._bestSol = peso_parziale
            self._bestPath = copy.deepcopy(parziale)

        vicini = self._grafo.neighbors(partenza)
        for v in vicini:
            peso = self._grafo[partenza][v]["weight"]
            if self.filtroNodi(v, parziale):

                parziale.append((partenza, v, peso))
                self._ricorsione(v, parziale)
                parziale.pop()


    def filtroArchi(self, u, v, parziale):
        for e in parziale:
            if e[:2] == (u, v) or e[:2] == (v, u):
                return False
        return True

    def calocaPesoParziale(self, parziale):
        pesoTot = 0
        for e in parziale:
            pesoTot += e[2]
        return pesoTot

    def filtroNodi(self, n, parziale):
        for e in parziale:
            if e[0] == n or e[1] == n:
                return False
        return True
