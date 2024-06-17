from model.model import Model

myModel = Model()
myModel.crea_grafo()
print(myModel.getGraphDetails())
res = myModel.getConnesse("golgi")
for r in res:
    print(r)