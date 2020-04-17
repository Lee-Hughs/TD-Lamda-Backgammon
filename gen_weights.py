#!C:\Users\Lee\AppData\Local\Programs\Python\Python38-32\python.exe
import random
import json

#mode = list noting the number of nodes per layer ie: ([9900, 50, 1]) for our case of 9900 input nodes, one hidden layer with 50 nodes, and one output layer
def gen_weights(model):
    #for each layer
    weights = []
    for a in range(len(model)):
        layer = []
        #for each node in the layer
        for b in range(model[a]):
            node = []
            #if we are not one the last layer
            if( a < len(model) - 1 ):
                #for node in the next layer
                for x in range(model[a+1]):
                    node.append(round(random.uniform(-4,4),2))
            layer.append(node)
        weights.append(layer)
    return weights

if __name__ == '__main__':
    model = [198,50,1]
    weights = gen_weights(model)

    with open("weights.json","w") as weight_file:
        weight_file.write(json.dumps(weights))
        weight_file.close()
        



