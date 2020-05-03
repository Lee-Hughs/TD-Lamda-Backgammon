#!C:\Users\leehu\AppData\Local\Programs\Python\Python37\python.exe
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
                    node.append(round(random.uniform(-1,1),4))
            layer.append(node)
        weights.append(layer)
    return weights

if __name__ == '__main__':
    biases = []
    for x in range(51):
        biases.append(round(random.uniform(-2,2),4))


    with open("bias.json","w") as bias_file:
        bias_file.write(json.dumps(biases))
        bias_file.close()
        



