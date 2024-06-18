from model.model import Model

myModel = Model()
myModel.crea_grafo()
print(myModel.getGraphDetails())
res = myModel.getnNeighboors("golgi")
"""for r in res:
    print(r)
    """
cammino, sol = myModel.handlePath("ER")
print("Peso soluzione: ", sol)
print("Cammino con partenza: ", "ER")
for c in cammino:
    print(c)