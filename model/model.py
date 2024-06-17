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

    def getConnesse(self, localizzazione):
        connessa = nx.node_connected_component(self._grafo, localizzazione)
        connessa = list(connessa)
        result = []
        for n in connessa:
            vicini_list = []
            vicini = self._grafo.neighbors(n)
            for v in vicini:
                vicini_list.append((v, self._grafo[n][v]["weight"]))
            result.append((n, vicini_list))
        return result